from modelle.gericht import Gericht


class Getraenk(Gericht):
    def __init__(self, id, name, portionsgroesse, preis, alkoholgehalt):
        self.alkoholgehalt = alkoholgehalt
        super().__init__(id, name, portionsgroesse, preis)

    def __str__(self):
        return f'Getränk: {self.id} | {self.name} | {self.portionsgroesse} | {self.preis} | {self.alkoholgehalt} '
