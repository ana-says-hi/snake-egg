from ui.code_for_ui import startup
from tests.hinzufugen_gericht import gericht_test
from tests.k_aktualisieren import test_aktualisieren
from tests.suche_k_inkompAdresse import k_finden_adresse
from tests.suche_k_inkompName import k_finden_name

gericht_test()
test_aktualisieren()
k_finden_adresse()
k_finden_name()
print("ALL TESTS PASSED SUCCESSFULLY")
startup()
