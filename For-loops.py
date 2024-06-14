# Die For-Schleife - 2 Varianten möglich:
# Mithilfe einer for-Schleife über ein iterierbares (= wiederholendes) Objekt laufen.
# Die for-Schleife in Kombination mit der Funktion range() als Zählerschleife einsetzen.

# Variante 1:
# Der schleifenkopf ist die erste Zeile.
# Nach dem Schlüsselwort "for" kommt immer ein Bezeichner, den man natürlich beliebig bezeichnen kann.
# Nach dem Bezeichner kommt das Schlüsselwort "in".
# Daraufhin folgt dann ein iterierbares Objekt, über welches man drüberlaufen möchte.
# Was ist ein iterierbares Objekt? Etwas, das ich durchlaufen kann. Zum Beispiel die 2 Datentypen string und list.
# Mit dem Start der for-Schleife wird jetzt jedes Element des iterierbaren Objekts, was in diesem Fall die Liste ist,
# mit jeweils einem eigenen Schleifendurchlauf, durchlaufen.
# Mithilfe des Bezeichners kann ich innerhalb des Schleifenkörpers auf das jeweilige Element, je nachdem in welchen
# Durchlauf ich gerade bin, zugreifen.
# Wenn also das erste mal der Schleifenkörper durchlaufen wird, dann greife ich mit dem Bezeichner auf das erste
# Element im iterierbaren Objekt zu. In diesem Fall ist es die 2.
# Wenn dieser Schleifenkörper durchgelaufen ist, dann bin ich wieder im Schleifenkopf und der nächste Schleifendurchlauf
# startet. Im zweiten Schleifendurchlauf greife ich auf das zweite Element, nämlich die 4 zu und so weiter...
for element in [2, 4, 6, 8]:  # Schleifenkopf
    print(element)  # Schleifenkörper

print("Jetzt kommt eine weitere for-Schleife.")

# Das gleiche mit einem string:
# Jeder Buchstabe und Leertaste wird einzelnd ausgegeben.
# Das erste Element ist der Buchstabe und so weiter...
for string in "Das ist ein String":
    print(string)


# Variante 2: # Die for-Schleife in Kombination mit der Funktion range() als Zählerschleife einsetzen.
# Der Aufbau der for-Schleife bleibt exakt der gleiche. Nur anstelle des iterierbaren Objekts kommt die range() Funktion
# Dieser Funktion kann man gewisse Parameter übergeben.
# Die Funktion, mit dem Parameter 10, erzeugt ein iterierbares Objekt, welches Werte von 0-9 enthält. Also 10 Durchläufe
# for Bereich in range(10):
    # print(Bereich)

# Hier soll der Startwert 3 und der Endwert 10 sein:
# Hier wird als Rückgabewert in der Konsole ein iterierbares Objekt erzeugt, welches Werte von 3-9 enthalten.
# Der Startwert, in dem Fall 3, wird im iterierbaren Objekt inkludiert, während der Endwert exkludiert wird.
# Wichtig: Die Standard-Schrittweite ist immer 1. Ich kann die Schrittweite jedoch ändern.
for numbers in range(3, 10):
    print(numbers)

print("Hier geht es Weiter...")

# Änderung der Schrittweite: Der dritte Parameter bestimmt die Höhe der Schrittweite.
for change in range(4, 36, 2):
    print(change)  # Konsole: erster Durchlauf ist die 4. Zweiter Durchlauf ist die 6 und so weiter... Bis zu 34...

# Das gleiche funktioniert auch mit negativen Schritten.
for negative in range(10, 3, -2):
    print(negative)  # Konsole/Rückgabewert/iterierbares Objekt: 10, 8, 6 und 4.
