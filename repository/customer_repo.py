from repository.data_repo import DataRepo
from modelle.kunde import Kunde


class CustomerRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, liste):  # elem: id, name, adresse
        li = map(lambda data: "|".join([data.id, data.name, data.adresse]), liste)
        return "\n".join(li)

    def convert_from_string(self, striing):
        def t(line):
            try:
                return Kunde(line.split("|")[0], line.split("|")[1], line.split("|")[2])
            except Exception as ex:
                asd = 0
        if striing != '':
            lines = striing.split("\n")
            liste = map(t, lines)
        else:
            liste = []
        return liste
