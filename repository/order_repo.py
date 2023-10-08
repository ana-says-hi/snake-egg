from repository.data_repo import DataRepo
from modelle.bestellung import Bestellung


class OrderRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, liste):
        # elem:  id, kunden_id, liste_id_ger= Gericht(), liste_id_getr= Getraenk()
        return "\n".join(
            list(map(lambda el: str(el.id) + "|" + str(el.kunden_id) + "|" + ",".join(
                list(map(lambda ids: str(ids), el.liste_id_ger))) +
                                "|" + ",".join(
                list(map(lambda ids: str(ids), el.liste_id_getr))) +
                                "|" + str(el.gesamtkosten), liste)))

    def convert_from_string(self, string):
        liste = []
        if string != '':
            lines = string.split("\n")
            liste = list(
                map(lambda line: Bestellung(line.split("|")[0], line.split("|")[1],
                                            list(line.split("|")[2].split("\n")[0].split(",")),
                                            list(line.split("|")[3].split("\n")[0].split(",")), line.split("|")[4]), lines))
        return liste
