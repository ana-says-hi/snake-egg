from modelle.gericht import Gericht


class GekochterGericht(Gericht):
    def __init__(self, id, name, portionsgroesse, preis, zubereitungszeit):
        self.zubereitungszeit = zubereitungszeit
        super().__init__(id, name, preis, portionsgroesse)

    def __str__(self):
        return f'Gekochter Gericht: {self.id} | {self.name} | {self.portionsgroesse} | {self.preis} | {self.zubereitungszeit} '
