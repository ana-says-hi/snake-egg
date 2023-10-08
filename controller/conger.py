from modelle.gekochter_gericht import GekochterGericht
from modelle.getrank import Getraenk
from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import GetrankRepo

gerichtRepo = CookedDishRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuMancare.txt")
getrankeRepo = GetrankRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuBauturi.txt")


def gericht_hinzufugen(new_Rec):
    if type(new_Rec) == GekochterGericht:
        gerichtRepo.save([new_Rec])
    else:
        getrankeRepo.save([new_Rec])


# gericht nu au nume
def gericht_anzeigen(strinng):
    foodListe = gerichtRepo.load()
    drinkListe = getrankeRepo.load()
    for food in foodListe:
        if strinng.lower() in food.name.lower():
            return food
        else:
            for drink in drinkListe:
                if strinng.lower() in drink.name.lower():
                    return drink


#
def gericht_finden(what_id, nr):  # soll keine fragen stellen
    if nr == 1:
        my_list = gerichtRepo.load()
    elif nr == 2:
        my_list = getrankeRepo.load()
    for food in my_list:
        if food.id == what_id:
            return food

        def fun(variable):
            new_list = map(lambda obj: obj.id, my_list)
            if variable in new_list:
                return True
            else:
                return False

    filtered = filter(fun, my_list)
    return filtered
    #print("ERROR: CONSUMABLE NOT FOUND")


def gericht_in_list(dish, liste):
    for gericht in liste:
        return gericht == dish


def gericht_aktualisiereen(dish):  # id, preis, portionsgroesse
    what_id = dish.id
    new_name = dish.name
    new_price = dish.price
    new_portion = dish.portionsgroesse
    foodListe = gerichtRepo.load()
    drinkListe = getrankeRepo.load()
    print("Was wollen Sie aktualisieren?")
    print("1. Preis \n"
          "2. Portionsgrösse")
    if gericht_in_list(dish, foodListe):  # sau type(dish)
        print("3. Zubereitungszeit")
        new_zub = dish.zubereitungszeit
        option = input("*")
        if option == 1:
            new_price = input("Wie viel soll sie kosten?")
        else:
            if option == 2:
                new_portion = input("Wie viel wiegt sie?")
            else:
                if option == 3:
                    new_zub = input("Wie viel werden die Kunden dafür warten?")
                else:
                    print("Invalid option")
        gericht_loeschen(dish)
        new_dish = GekochterGericht(what_id, new_name, new_price, new_portion, new_zub)
        gericht_hinzufugen(new_dish)

    elif gericht_in_list(dish, drinkListe):  # drink
        print("3. Alkoholgehalt")
        new_alc = dish.alkoholgehalt
        option = input("*")
        if option == 1:
            new_price = input("Wie viel soll sie kosten?")
        else:
            if option == 2:
                new_portion = input("Wie viel wiegt sie?")
            else:
                if option == 3:
                    new_alc = input("Wie viel Alkohol enthält das?")
                else:
                    print("Invalid option")
        gericht_loeschen(dish)
        new_dish = Getraenk(what_id, new_name, new_price, new_portion, new_alc)
        gericht_hinzufugen(new_dish)


def gericht_loeschen(dish):
    new_menu = []
    foodListe = gerichtRepo.load()
    drinkListe = getrankeRepo.load()
    if dish in foodListe:
        my_repo = gerichtRepo
    elif dish in drinkListe:
        my_repo = getrankeRepo
    else:
        print("ERROR404: CONSUMABLE NOT FOUND")
        return 0
    dishez = my_repo.load()
    for ger in dishez:
        if ger == dish:
            pass
        else:
            new_menu.append(ger)
    my_repo.write_in_file(new_menu)
