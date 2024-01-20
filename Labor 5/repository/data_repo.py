import abc


class DataRepo:
    def __init__(self, datei):
        self.datei = datei

    # + save(speichert eine Liste von Objekten in einer Datei)
    # ~ load(liest eine Liste von Objekten aus einer Datei)
    # + read file(liest den Inhalt einer Datei und gibt ihn zurück)
    # + write to file(schreibt einen String in eine Datei und überschreibt die Datei)

    def save(self, liste):
        # print(self.convert_to_string(liste))
        f = open(self.datei, "a")
        f.write("\n")
        f.write(self.convert_to_string(liste))
        f.close()

    def load(self):
        return self.convert_from_string(self.read_file())

    def read_file(self):
        string = ""
        with open(self.datei) as f:
            for line in f:
                string = string + line
        return string

    def write_in_file(self, liste):
        f = open(self.datei, "w")
        f.write(self.convert_to_string(liste))
        f.close()

    @abc.abstractmethod
    def convert_to_string(self, liste):
        pass

    @abc.abstractmethod
    def convert_from_string(self, string):
        pass
