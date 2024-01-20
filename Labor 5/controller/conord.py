from repository.order_repo import OrderRepo

ordRepo = OrderRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Order.txt")


def order_hinzufugen(new_Order):
    ordRepo.save([new_Order])

def order_lesen():
    liste = ordRepo.load()
    return liste
