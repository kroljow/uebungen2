# Anzahl der Kisten und Kapazität pro Fahrt
anzahl_kisten = 1000
kapazitaet_pro_fahrt = 75

# Berechne die Anzahl der Fahrten
anzahl_fahrten = anzahl_kisten // kapazitaet_pro_fahrt

# Berechne die Anzahl der Kisten in der letzten Fahrt
kisten_in_letzter_fahrt = anzahl_kisten % kapazitaet_pro_fahrt

# Ausgabe der Ergebnisse
print("Das Unternehmen benötigt", anzahl_fahrten, "Fahrten, um alle Kisten zu transportieren.")
print("In der letzten Fahrt sind", kisten_in_letzter_fahrt, "Kisten.")
