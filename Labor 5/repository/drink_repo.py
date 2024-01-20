from repository.data_repo import DataRepo
from modelle.getrank import Getraenk


class GetrankRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, liste):  # elem: id, portionsgroesse, preis, alkoholgehalt
        return "\n".join(
            list(map(lambda el: str(el.id) + "|" + el.name + "|" + str(el.portionsgroesse) + "|" + str(
                el.preis) + "|" + str(el.alkoholgehalt), liste)))

    def convert_from_string(self, string):
        liste = []
        if string != '':
            lines = string.split("\n")
            liste = list(map(lambda line: Getraenk(line.split("|")[0], line.split("|")[1], line.split("|")[2],
                                                   line.split("|")[3], line.split("|")[4]), lines))
        return liste
