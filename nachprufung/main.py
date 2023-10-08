# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt
import functools


# 2.a 2 Punkte
# 2.b 2 Punkte

# 3. 1 Punkt
# Insgesamt: 9 Punkte

# 1.
# Geben Sie eine Textdatei mit dem Namen 'text.txt' an, die in jeder Zeile den Vor- und Nachnamen des Schülers,
# das Fach und die jeweilige Note enthält. Die Felder sollen durch drei Strichpunkt (';;;') voneinander getrennt sein.
# Schreiben Sie eine Funktion namens 'ub1', die folgendes tut:
#  - liest aus der angegebenen Datei 'text.txt'
#  - behält nur die Zeilen, bei denen der Nachname eine Länge von 3 hat und die Note eine gerade Zahl ist (0,5 Punkte)
#  - gibt einen String aller Fächer aus den behaltenen Zeilen zurück. Die Fächer sollen in Kleinbuchstaben und durch
#    Kommas getrennt sein. (0,5 Punkte)
# Die Verwendung von for- oder while-Schleifen, list comprehension ist nicht erlaubt. Es wird erwartet,
# dass die Lösung map, filter, reduce und andere mathematische Operationen, falls erforderlich, verwendet. (2 Punkte)

# schuler= vorname, nachname, fach, note

def ub1():
    fisier = open("text.txt", "r")
    file = list(map(lambda line: line.split("\n")[0], fisier))
    kinder = list(map(lambda line: line.split(';;;'), file))
    # print(kinder)
    answerkinder = filter(lambda kind: len(kind[1]) == 3 and int(kind[3]) % 2 == 0, kinder)
    # print(answerkinder)
    return functools.reduce(lambda a, b: a[2].lower() + ", " + b[2].lower(), answerkinder)


print(ub1())


# stri="Aaa"
# print(stri.lower())

# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.

def test_passed():
    assert ub1() == "Advanced programming, Programming fundamentals"


def test_failed():
    assert ub1() == "Vocal Training"


# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "Student". Die Klasse sollte in der Lage sein,
# Folgendes zu tun:
# - Bei der Initialisierung wird die Instanzvariable "grades" auf einen gegebenen Parameter gesetzt.
# - Der Typ des Parameters ist eine Liste von Zahlen. (0,5 Punkte)
# - Eine Methode namens "take_exam" haben, die:     book->students
#   - Einen einzelnen String-Parameter namens "exam" bekommt
#   - Für alle Elemente aus der Liste "grades" prüft, ob alle größer oder gleich 5 sind (0,5 Punkte)
#   - Eine neue Liste zurückgibt, die nur ein Element enthält, und zwar ein Tuple, gebildet aus dem Parameter "exam"
#     und dem ersten Element der Liste "grades" (0,5 Punkte)
#   - Eine benutzerdefinierte Ausnahme namens "FailedExam" wirft, wenn kein Element größer oder gleich 5 ist(0,5 Punkte)


# b. Schreiben Sie die Definition für eine Klasse namens "ComputerScienceStudent", die von "Student" erbt.
# Die Klasse sollte Folgendes können:
# - Bei der Initialisierung setzt sie neben den Variablen von "Student" auch eine Instanzvariable namens "laptop" auf ein
#   leeres Wörterbuch (dict). (0,25 Punkte)
# - Überschreiben der Methode "take_exam", um Folgendes zu tun:
#   - Wiederverwendung der Methode "take_exam" aus der Basisklasse (0,25 Punkte)
#   - Im Falle eines erfolgreichen Aufrufs wird das Ergebnis in der Instanzvariable "laptop" gespeichert, wobei der
#     Schlüssel und der Wert das erste beziehungsweise zweite Element des Tupels sind (0,25 Punkte)
#   - Im Falle eines fehlgeschlagenen Aufrufs wird in der Instanzvariable "laptop" ein Eintrag hinzugefügt, wobei der
#     Schlüssel der Parameter "exam" ist und der Wert 0 ist (0,25 Punkte)
# - Das Ergebnis der Addition zwischen zwei Instanzen des Typs "ComputerScienceStudent" (stud1 + stud2)
# ist ein Wörterbuch, das alle Einträge der beiden "laptop"-Instanzvariablen enthält.
#   Die Priorität der Einträge ist nicht wichtig. (1 Punkt)


# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(n):
    lst = []
    total = 0
    for i in range(-n, n):
        print(i, end=',')
        if i % 10 == 0:
            total += i
            # print(total, end='  ')
        lst.append(total)
    return lst


def my_func2(n):
    if n == 0:
        return [0]
    else:
        if n % 10 == 0:
            return [n] * 10 + my_func2(n - 1)
        else:
            return my_func2(n - 1)


def my_func2(n):
    if n == 0:
        return []
    if n < 10:
        return n*2*[0]
    if n % 10 == 0:
        return my_func2(n - 1) + [-n] * n*2 + my_func2(n - 1)
    return my_func2(n - 1)

print(my_func(0))
print(my_func2(0))
print(my_func(10))
print(my_func2(10))
print(my_func(2))
print(my_func2(2))
