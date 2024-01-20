from modelle.bestellung import Bestellung
from controller.conord import order_lesen, order_hinzufugen
from repository.order_repo import OrderRepo

ordRepo = OrderRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Order.txt")

def new_order_test():
    b = Bestellung("0980", "1212", ["3478"], ["3786"], "0")
    b.anzeigenRechnung()
    order_hinzufugen(b)
    b2 = Bestellung("0853", "1872", ["3478"], ["3786"], "0")
    b2.anzeigenRechnung()
    order_hinzufugen(b2)
    ordRepo.write_in_file([])
    print(ordRepo.read_file())


def read_order_test():
    b = Bestellung("0980", "1212", ["3478"], ["9087", "3671"], "0")
    b.anzeigenRechnung()
    order_hinzufugen(b)
    b2 = Bestellung("0853", "1872", ["3478"], ["9087"], "0")
    b2.anzeigenRechnung()
    order_hinzufugen(b2)
    l=ordRepo.load()
    if b in l:
        print("yay")
    ordRepo.write_in_file([])
read_order_test()
new_order_test()