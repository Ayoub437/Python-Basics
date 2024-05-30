# Fallunterscheidungen/Verzweigungen:
# In einer Variable etwas speichern, dass der Nutzer in das Programm eingeben kann. Er soll eine Ganzzahl eingeben.
number = int(input("Bitte gebe eine Ganzzahl ein: "))

# Dieses "if" ist ein Schlüsselwort. Nach jedem Schlüsselwort kommt eine Bedingung.
# Diesen Codeblock nennt man if-Block.
if number < 10:  # "number < 10" ist eine Bedingung.
    print("Die eingegebene Zahl ist kleiner als 10.")  # Diesen Codeblock nennt man Anweisungskörper oder
    # Das ist ein else-Zweig.
else:
    # Wieder Anweisungskörper
    print("Die eingegebene Zahl ist 10 oder größer als 10.")

# Es kann ein direkter Wahrheitswert True oder False als Bedingung drinne stehen. Z.b. if True:
# Oder auch eine Variable. Z.b. variable = False -- if variable:
# Wichtig ist, dass bei der Auswertung der Bedingung durch den Computer ein Wahrheitswert das Resultat sein muss.
# Das Ergebnis der Bedingung muss entweder True oder False sein.


# Hier kommt jetzt das elif-Zweig:
# Sobald eine Bedingung True, wird der damit verbundene Anweisungskörper ausgeführt.
# elif steht für else-if.
# Beispielaufgabe mit elif:

size_number = int(input("Bitte gib deine Hemdgröße ein: "))

if size_number == 1:
    print("Deine Hemdgröße ist 1.")  # Wenn dieser Vergleich nicht stimmt, ist er False.
elif size_number == 2:
    print("Deine Hemdgröße ist 2.")
elif size_number == 3:
    print("Deine Hemdgröße ist 3.")
else:
    print("Die eingegebene Zahl ist entweder 0 oder größer als 3.")

# Die elif-Verzweigungen kann man problemlos mit einem weiteren if-Block ersetzen.
# Warum mache ich das dann nicht? Wegen der schlechten Übersicht.
# Da ich dann nicht weiß ob die alle in gewisser Art und Weise zusammengehören oder ob Sie einzelnd für sich betrachtet
# Sinn ergeben würden.
# Der elif-Zweig wird eingesetzt, wenn davor ein if steht.
# Ein weiterer Grund ist, das der Computer bei nacheinander stehenden if-Blöcke, selbst die if-Blöcke auswertet die
# False sind.
# Bei elif-Zweigen werden die Bedingungen von oben nach unten ausgewertet und nachdem die Bedingung mit True
# gefunden wurde, ignoriert er die anderen Bedingungen.
# Die elif-Zweige sind also effizienter als nacheinander stehende if-Blöcke, da Sie Zeit spart.

print("Hier gehts weiter")


# Eine weitere Aufgabe
# Die Print-Ausgabe ist an eine einfache Bedingung geknüpft.
# Für diese Abfrage/Bedingung benötigt 4 Zeilen Code. Um das ganze Abzukürzen benutze ich einen bedingten Ausdruck.

bill = 10

Tip_Trinkgeld = float(input("Rechnung: " + str(bill) + " Euro, wie viel Trinkgeld möchten Sie geben?: "))

if Tip_Trinkgeld < bill * 0.1:  # "bill * 0.1" -> die 0.1 stellt die 10% Trinkgeld dar, die in Deutschland gelten.
    print("Vielen Dank!")
else:
    print("Wow, vielen lieben Dank! Sehr großzügig!")


# Jetzt kommt das Thema "Bedingte Ausdrücke"/ conditional expression:
# Bei dem bedingten Ausdruck ist es wichtig, das die Bedingung ein logischer Ausdruck sein muss. Es muss also der
# Rückgabewert bei True oder False nach der Auswertung des logischen Ausdrucks zurückgegeben werden.
# Ich kann einen beliebigen Ausdruck rein schreiben, z.b. eine Rechnung. Also nicht nur auf eine Print-Anweisung.
# "Bedingter Ausdruck" ist etwas schwerer lesbar als das if-else-Konstrukt.
# Mit dem if-else-Konstrukt ist es mehr Zeilen Code, aber dafür übersichtlicher.
# A if Bedingung else B -> Übersetzt: Mache A wenn die Bedingung wahr ist, ansonsten mache B
print("Vielen Dank!") if Tip_Trinkgeld < bill * 0.1 else print("Wow, vielen lieben Dank! Sehr großzügig!")
