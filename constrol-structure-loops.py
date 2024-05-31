# While-Schleife:
# Was ist eine While-Schleife?
# Mithile einer Schleife kann man gewisse Code-Blöcke beliebig oft wiederholen.

# "While" ist ein Schlüsselwort.
# Dieses Beispiel ist eine Endlosschleife, da die Schleife unendlich oft ausgeführt wird.
# Eine Schleife besteht immer aus einem Schleifenkopf.
# Bei Schleifen hat man Vergleiche als Bedingung stehen. -> "2 < 10"
# Da ich zwei Konstanten habe die ich miteinander vergleiche, wird die Schleifenbedingung immer True sein.
# Wenn der Schleifenkopf True ist wird der Schleifenkörper ausgeführt. Danach wird wieder geprüft, ob der Schleifenkopf
# True ist. Das geht immer so weiter.
# while 2 < 10:  # "while 2 < 10:" -> Das ist ein Schleifenkopf. In diesem Schleifenkopf ist die Bedingung definiert.
# print("Das ist eine Ausgabe ...")  # Das ist der Schleifenkörper.

# Eine weitere While-Schleife:
# Dadurch das sich die Variable bei jeder Ausführung um eine Zahl erhöht, bis es den Wert erreicht, der immernoch
# kleiner als 10 ist. Die Bedingung wird also 3 mal ausgeführt.
# Das ist keine Endlosschleife.
counter = 7
while counter < 10:
    print("Das ist eine Ausgabe ...")
    counter += 1  # Es wird so lange um 1 erhöht, bis es 10 erreicht und somit False ist. Die Schleife ist nach dem
    # dritten mal beendet.
