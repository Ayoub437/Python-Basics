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


# Die Schlüsselwörter break und continue:
# Jetzt möchte ich ein Programm, welches dem Nutzer nur 3 versuche gibt, um sein Password korrekt einzugeben.
# Hier möchte ich ein Formular programmieren, in welchem ein Nutzer aufgefordert wird, sein Password einzugeben.

password = "passwort123"
user_input = ""
counter = 0  # Das soll der Zähler sein, in welchem Versuch ich bin.

while user_input != password:  # Da die Bedingung True ist, wird der Schleifenkörper ausgeführt.
    if counter == 3:
        break  # Wenn break aufgerufen wird, wird der ganze Schleifenprozess abgebrochen. Würde dann bei print weiter...
    user_input = input("Bitte gebe das korrekte Password ein: ")  # Dieser Schleifenkörper wird im nächsten Durchlauf
    # erneut abgefragt, wenn das Passwort falsch ist.
    counter += 1  # Der Zähler soll um 1 erhöht werden, weil es jetzt im nächsten Versuch ist.
    # Wenn das Passwort korrekt eingegeben wurde, wird das Programm weiter laufen.

print("Das Password wurde korrekt eingegeben.")


# TASK 6: Das Schlüsselwort break im Zusammenhang mit einer while-Schleife:
# Ich möchte dafür sorgen, dass der Nutzer aufgefordert wird, sein passwort einzugeben.
# Jetzt möchte ich ein Programm, welches dem Nutzer nur 3 versuche gibt, um sein Password korrekt einzugeben.

passwort12 = "Hello123"
user_input12 = ""
counts = 0

while user_input12 != passwort12:
    if counts == 3:
        break
    user_input12 = input("Bitte gebe das Passwort ein: ")
    counts += 1

print("Das Passwort wurde korrekt eingegeben...")

print("Hier geht es weiter")

# Eine weitere Möglichkeit ist, die Counter-abfrage in die Bedingung einzubauen.
# Wieder die selbe Aufgabe wie zuvor: ein Programm, welches dem Nutzer nur 3 versuche gibt, um sein Password korrekt
# einzugeben.
# Dafür kommt das if und das Schlüsselwort break weg.

passwort13 = "neo44"
user_input13 = ""
counter = 0

while passwort13 != user_input13 and counter < 3:
    user_input13 = input("Bitte gebe das korrekte Passwort ein: ")
    counter += 1

print("Das Passwort wurde korrekt eingegeben...")


# Diese Aufgabe gehört zur oberen:
# Eine Endlosschleife mit dem Schlüsselwort continue: Ohne break würde ich aus dieser Endlosschleife nicht
# mehr raukommen.
# Mithilfe von continue wird die Schleife nicht sofort beendet, sondern stattdessen wird nur der aktuelle
# Schleifendurchlauf, also die Abarbeitung des Schleifenkörpers beendet. Und dann wird erneut die Bedingung abgefragt.

while True:
    name = input("Bitte Nutzernamen eingeben: ")
    if name != "testUser":  # Wenn die Bedingung True ist, dann wird continue ausgeführt.
        continue  # Der Rest dieses Schleifendurchlaufs soll übersprungen werden./ Der untere Teil (Schleifenkörper)
        # wird nicht ausgeführt.
    user_input13 = input("Hallo testUser, was ist dein Passwort? ")  # Passwort wurde bereits oben definiert.
    if user_input13 == passwort13:
        break  # Der Schleifenprozess soll beendet werden, da ich erfolgreich eingeloggt wurde.

print("testUser wurde erfolgreich eingeloggt!")
