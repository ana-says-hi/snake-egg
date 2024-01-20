from modelle.identifizierbar import Identifizierbar
from controller.conger import gericht_finden
from controller.conkun import kunde_finden
from datetime import date, datetime


class Bestellung(Identifizierbar):

    def __init__(self, id, kunden_id, liste_id_ger, liste_id_getr, uhrzeit):
        super().__init__(id)
        self.kunden_id = kunden_id
        self.liste_id_ger = liste_id_ger
        self.liste_id_getr = liste_id_getr
        self.__gesamtkosten = 0
        self.lieferdatum = date.today()
        self.uhrzeit = datetime.now()

    @property
    def gesamtkosten(self):
        return self.__gesamtkosten

    @gesamtkosten.setter
    def gesamtkosten(self, gesamtkosten):
        self.__gesamtkosten = gesamtkosten

    def berehnungKosten(self):
        self.gesamtkosten = 0
        # self.gesamtkosten = functools.reduce(lambda a, b: gericht_finden(a).preis + gericht_finden(b).preis,
        #                                      self.liste_id_ger) + functools.reduce(
        #     lambda a, b: gericht_finden(a).preis + gericht_finden(b).preis, self.liste_id_getr)
        zahlung = list(map(lambda i: int(gericht_finden(i, 1).preis), self.liste_id_ger))
        zahlung2 = list(map(lambda i: int(gericht_finden(i, 2).preis), self.liste_id_getr))
        z = 0
        for zahl in zahlung:
            z += zahl
        for zahl in zahlung2:
            z += zahl
        self.gesamtkosten = z

    def __stringRechnung(self):
        self.berehnungKosten()
        print("\n".join(
            [",".join(
                map(lambda ids: gericht_finden(ids, 1).id + " " + gericht_finden(ids, 1).name, self.liste_id_ger)),
             "-----------",
             ",".join(
                 map(lambda obj: gericht_finden(obj, 2).id + " " + gericht_finden(obj, 2).name, self.liste_id_getr)),
             "============", "GESAMTKOSTEN = " + str(self.gesamtkosten),
             "Bestellung wurde gemacht um:"]))
        print(self.uhrzeit)

    def anzeigenRechnung(self):
        print("***" + self.id + "***")
        print(kunde_finden(self.kunden_id))
        self.__stringRechnung()

    def __str__(self):
        self.berehnungKosten()
        return f'Bestellung: {self.id} | {self.kunden_id} | Gesamtkosten: {self.gesamtkosten} \n' \
               f'     ------- \n' \
               f'{map(lambda i: print(gericht_finden(i, 1)), self.liste_id_ger)} \n' \
               f'     _______ \n' \
               f'{map(lambda i: print(gericht_finden(i, 2)), self.liste_id_getr)}\n' \
               f'==================================\n'
