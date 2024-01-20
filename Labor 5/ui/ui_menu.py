from repository.data_repo import DataRepo
from modelle.gekochter_gericht import GekochterGericht
from modelle.getrank import Getraenk
from controller.conger import gericht_hinzufugen, gericht_loeschen, gericht_aktualisiereen


def action():
    a = input("Was wollen Sie tun?")
    return a


def check_menu():
    print("Which menu are you going to open?")
    print("1. Food Menu")
    print("2. Drinks Menu")
    print("3. Update Menu")
    act = action()
    if act == '1':
        repo = DataRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuMancare.txt")
        print(repo.read_file())
    elif act == '2':
        repo = DataRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuBauturi.txt")
        print(repo.read_file())
    elif act == '3':
        update_menu()
    else:
        raise NotImplementedError("Pick one of the options above.")


def update_menu():
    print("\n")
    print("1. Gericht hinzufügen\n"
          "2. Gericht aktualisieren (id)\n"
          "3. Gericht löschen (id)\n"
          "\n"
          )
    act = action()
    if act == '1':
        print("Was wollen Sie hinzufügen?")
        ch = input("0. Gekochter Gericht \n1. Getränk")
        print("Antworten Sie, bitte, folgended Fragen:")
        i = input("ID eingeben: ")
        n = input("name: ")
        por = input("Wie groß ist eine Portion? ")
        pre = input("Wie viel kostet das? ")
        if ch == '0':
            zbs = input("Wie viel wird es dauern?")
            food = GekochterGericht(i, n, por, pre, zbs)
        else:
            alc = input("Wie viel Alkohol enthält das?")
            food = Getraenk(i, n, por, pre, alc)
        gericht_hinzufugen(food)

    elif act == '2':
        i = input("Für diese Operation brauchen wir den ID des Gerichtes")
        gericht_aktualisiereen(i)

    elif act == '3':
        i = input("Für diese Operation brauchen wir den ID des Gerichtes")
        gericht_loeschen(i)
    else:
        raise NotImplementedError("Pick one of the options above.")
