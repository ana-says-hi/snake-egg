from ui.ui_clients import clients
from ui.ui_menu import check_menu
from repository.order_repo import OrderRepo
from modelle.bestellung import Bestellung
from datetime import datetime
from controller.conord import order_lesen


def startup():
    while True:
        print("0. Exit\n"
              "1. Check Menu\n"
              "2. About Orders\n"
              "3. About Clients\n"
              )
        act = input("Was wollen Sie tun?")
        if act == '0':
            break
        elif act == '1':
            check_menu()
        elif act == '2':
            orders()
        elif act == '3':
            clients()
        else:
            raise NotImplementedError("Pick one of the options above")


def orders():
    order_repo = OrderRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Order.txt")
    print("1. New Order\n"
          "2. View Orders\n"
          )
    act = input("Was wollen Sie tun?")
    if act == '1':
        print("Antworten Sie, bitte, folgended Fragen:")
        i = input("Id (4 Ziffern):")
        i_k = input("Welcher ist der ID des Kundes?")
        lis_d = input("Welche Getränke hat dieser bestellt? (IDs)")
        lis_f = input("Was hat er gegessen? (IDs)")
        lis_f = lis_f.split(" ")
        lis_d = lis_d.split(" ")
        best = Bestellung(i, i_k, lis_f, lis_d, datetime.now().strftime("%H:%M:%S"))
        best.anzeigenRechnung()
    elif act == '2':
        lis = order_lesen()
        for elem in lis:
            elem.anzeigenRechnung()
            print("\n")

