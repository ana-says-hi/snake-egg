from controller.conkun import kunden_anzeigen, kunde_loeschen
from modelle.kunde import Kunde
from repository.customer_repo import CustomerRepo


def k_finden_adresse():
    client1 = Kunde("1951", "Maria", "Iasi")
    client2 = Kunde("1452", "David", "Sighisoara")
    repo = CustomerRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Kunden.txt")
    repo.save([client1, client2])
    c1 = kunden_anzeigen("IA", "1")
    c2 = kunden_anzeigen("ghisoara", "1")
    assert c1 == client1
    kunde_loeschen(client1)
    assert c2 == client2
    kunde_loeschen(client2)


k_finden_adresse()

