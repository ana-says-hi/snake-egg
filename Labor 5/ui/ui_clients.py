from controller.conkun import kunde_hinzufugen, kunden_anzeigen, kunde_finden, kunde_aktualisieren, kunde_loeschen
from modelle.kunde import Kunde


def action():
    a = input("Was wollen Sie tun?")
    return a


def clients():
    print("\n")
    print("1. Kunde hinzufügen\n"
          "2. Kunde anzeigen\n"
          "3. Kunde aktualisieren (id)\n"
          "4. Kunde löschen (id)\n"
          "\n"
          )
    act = action()

    if act == '1':
        print("Antworten Sie, bitte, folgended Fragen:")
        nam = input("Wie heißt dieses Person?")
        adr = input("Wo wohnt diese Person?")
        i = input("Id (4 Ziffern):")
        k = Kunde(i, nam, adr)
        print(kunde_hinzufugen(k))

    elif act == '2':
        cuv = input("Was suchen wir?")
        qu = input("Ist das der Name des Kundes oder seine Adresse? \n [0-Name, 1-Adresse]")
        print("Der beste Resultat der Suche ist:")
        print(kunden_anzeigen(cuv, qu))

    elif act == '3':
        i = input("Für diese Operation brauchen wir den ID der Person")
        print("Was wollen Sie aktualisieren?")
        options = input("1. Name \n"
                        "2. Adresse\n")
        if options == '1':
            what = input("Wie heißen Sie jetzt?")
        else:
            if options == '2':
                what = input("Wo wohnen Sie jetzt?")
            else:
                print("Invalid option")
        print("SUCCESSFULLY UPDATED:")
        print(kunde_aktualisieren(i, options, what))



    elif act == '4':
        i = input("Für diese Operation brauchen wir den ID der Person")
        kunde_loeschen(i)

    else:
        raise NotImplementedError("Pick one of the options above")
    print('\n')
