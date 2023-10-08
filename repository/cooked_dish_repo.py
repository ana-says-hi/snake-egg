from repository.data_repo import DataRepo
from modelle.gekochter_gericht import GekochterGericht


class CookedDishRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, liste):  # elem: id, portionsgroesse, preis, zubereitungszeit
        return "\n".join(
            list(map(lambda el: "|".join([el.id, el.name, el.portionsgroesse, el.preis, el.zubereitungszeit]), liste)))

    def convert_from_string(self, string):
        liste = []
        if string != '':
            lines = string.split("\n")
            liste = list(
                map(lambda line: GekochterGericht(line.split("|")[0], line.split("|")[1], line.split("|")[2],
                                                  line.split("|")[3], line.split("|")[4]), lines))
        return liste
