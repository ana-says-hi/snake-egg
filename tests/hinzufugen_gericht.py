from controller.conger import gericht_hinzufugen, gericht_loeschen
from repository.cooked_dish_repo import *
from repository.drink_repo import *


def gericht_test():
    repo = CookedDishRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuMancare.txt")
    r1 = GekochterGericht("2456", "Essen", "350g", "20", "30")
    gericht_hinzufugen(r1)
    r2 = Getraenk("9456", "Saft", "500l", "15", "0%")
    gericht_hinzufugen(r2)
    l1 = repo.load()
    for i in l1:
        if i == r1:
            ree1 = i
    assert ree1 == r1
    gericht_loeschen(r1)
    repo = GetrankRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\MeniuBauturi.txt")
    l1 = repo.load()
    for i in l1:
        if i == r2:
            ree2 = i
    assert ree2 == r2
    gericht_loeschen(r2)

gericht_test()
