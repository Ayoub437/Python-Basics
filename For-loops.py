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
