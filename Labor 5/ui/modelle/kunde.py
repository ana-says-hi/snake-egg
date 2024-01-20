from modelle.identifizierbar import Identifizierbar


class Kunde(Identifizierbar):
    def __init__(self, id, name, adresse):
        self.name = name
        self.adresse = adresse
        super().__init__(id)

    def __str__(self):
        return f'Kunde: {self.id} | {self.name} | {self.adresse} '

    def __eq__(self, other):
        return self.id == other.id
