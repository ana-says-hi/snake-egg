class FailedExam(Exception):
    pass


class Student:
    def __init__(self, grades: []):
        self.grades = grades

    def take_exam(self, exam):
        lis_tup = []
        ok = 0
        for note in self.grades:
            if note >= 5:
                ok += 1
        lis_tup.append((exam, self.grades[0]))
        if ok == 0:
            raise FailedExam
        return lis_tup

class ComputerScienceStudent(Student):
    def __init__(self, grades, laptop={}):
        super().__init__(grades)
        self.laptop = laptop

    def take_exam(self, exam):
        try:
            laptop = super().take_exam(exam)
            aux1, aux2 = laptop[0]
            self.laptop[aux1] = aux2
        except:
            self.laptop[exam] = 0

    def __add__(self, other):
        wortb = {}
        for elem in self.laptop:
            wortb[elem.key()] = elem.value()
        for elem in other.laptop:
            wortb[elem.key()] = elem.value()
        return wortb


class Money:
    def __init__(self, value, currency):
        self.value=value
        self.currency=currency

    def transform(self,new_unit):
        if self.currency=="RON" and new_unit=="EURO":
            return Money(self.currency*4.9, new_unit)
