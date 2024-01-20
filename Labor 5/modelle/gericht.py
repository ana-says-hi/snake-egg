from modelle.identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    def __init__(self, id, name, preis, portionsgroesse):
        self.name = name
        self.preis = preis
        self.portionsgroesse = portionsgroesse
        super().__init__(id)

    def __str__(self):
        return f'Gericht: {self.id} | {self.portionsgroesse} | {self.preis} '

    def __eq__(self, other):
        return self.id == other.id
