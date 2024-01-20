from modelle.kunde import Kunde
from repository.customer_repo import CustomerRepo

kundenRepo = CustomerRepo("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Kunden.txt")


def kunde_hinzufugen(new_Customer):  # id, name, adresse
    kundenRepo.save([new_Customer])


def kunden_anzeigen(strinng, question):
    kundenListe = kundenRepo.convert_from_string(kundenRepo.read_file())
    if question == "0":
        client_l = list(filter(lambda client: strinng.lower() in client.name.lower(), kundenListe))
    if question == "1":
        client_l = list(filter(lambda client: strinng.lower() in client.adresse.lower(), kundenListe))
    return client_l[0]
    # for client in kundenListe:
    #     # if strinng.lower() in client.name.lower() and question == "0":
    #     #     return client
    #     else:
    #         if strinng.lower() in client.adresse.lower() and question == "1":
    #             return client


def kunde_finden(what_id):
    kundenListe = kundenRepo.convert_from_string(kundenRepo.read_file())
    for client in kundenListe:
        if client.id == what_id:
            return client
    return "ERROR: CLIENT NOT FOUND"


def kunde_aktualisieren(client, options, what):
    what_id = client.id
    new_name = client.name
    new_address = client.adresse
    if options == '1':
        new_name = what
    else:
        if options == '2':
            new_address = what
    kunde_loeschen(client)
    new_client = Kunde(what_id, new_name, new_address)
    # f = open("C:\\Users\\Ana\\PycharmProjects\\Labor_5\\database\\Kunden.txt", "a")
    # f.write('\n')
    # f.close()
    kunde_hinzufugen(new_client)
    return new_client


def kunde_loeschen(to_del):
    clients = []
    kunden = kundenRepo.load()
    for kun in kunden:
        if kun == to_del:
            pass
        else:
            clients.append(kun)
    kundenRepo.write_in_file(clients)
