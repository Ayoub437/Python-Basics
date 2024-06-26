# TASK 1: Write a program which you can use to track people.
# First of all, the user's first name shall be prompted(=abgefragt) and read.
# After that, the same with the surname and age of the user.
# As soon as the values are read in, the full name and age shall be executed in the console.

# first name
# I add strings to let the user know what is expected from him.
# Type-casting is not necessary, because the type inside the input-function is a string anyway.
# I did type-casting and stored the variable age as integer, because it can cause
# confusion if I extend the program and age was stored as a string.
first_name = input("Please enter surname: ")
last_name = input("Please enter your last name: ")
# I add type-casting-function to store an integer to variable "age".
age = int(input("Please enter the age: "))
# I do type-casting to variable age, because the program can only concatenate(=verbinden) str to str and not str to int.
print(first_name + " " + last_name + " is " + str(age) + " years old.")


# TASK 2: Extend this program so that the user is asked to enter the value 0,
# if he wants to output(=ausgeben) the name "Lars Mustermann".
# If he wants to output the name "Fritz Huber", the user shall enter the value 1.
# In "Lisa Neumann's" case, the user shall enter the value 2.
first_names = ["Lars", "Fritz", "Lisa"]
last_names = ["Mustermann", "Huber", "Neumann"]

output = int(input("Please enter a number between 0 and 2: "))
# By adding the variable "output", it is programmed in a more generic way.
# Now, the output in console is always that what is read in by the user in input-function.
# If I change the "output" to the index 0, it always stays 0 and always "Lars Mustermann" is printed,
# because then it is "hart kodiert".
print(first_names[output] + " " + last_names[output])


# TASK 3: Wenn man im Supermarkt an einer Kasse arbeitet, hat man neben der Tätigkeit des Kassierens auch die Aufgabe,
# für gewisse Produkte das Alter des Kunden zu prüfen (z.b. Tabakwaren, Alkohol). Hierzu muss der Kunde seinen
# Personalausweis vorzeigen, auf welchem sein Geburtsdatum angegeben ist. Auf Basis des Jahrgangs in wenigen Sekunden
# zu entscheiden, ob der Kunde nun schon 18 Jahre oder älter ist, kann häufig zu Fehlern führen.
# Aus diesem Grund möchten wir ein kleines vereinfachtes Programm schreiben, in welchem man den Jahrgang des Kunden
# eintippt und daraufhin True oder False zurückgegeben bekommt. (Hinweis: Ich führe eine vereinfachte Prüfung durch,
# was bedeutet, dass wir wirklich nur den Jahrgang prüfen. Wenn beispielsweise also jemand am 23.04.2003 geboren ist,
# dann soll nur auf Basis des Jahrgangs (in diesem Fall 2003) geprüft werden, ob der Kunde schon 18 ist oder eben nicht)

# Bei der input-Funktion soll der Kassierer aufgefordert werden, den Jahrgang des Kunden einzugeben.
# Hier caste ich direkt einen integer.
# Ergebnis: Abhängig von dem Jahrgang, welches ich in der Konsole eingebe. Kann True oder False sein
current_year = 2024
year_of_birth = int(input("Jahrgang eingeben: "))
print(current_year - year_of_birth >= 18)  # Console: Die Differenz zwischen 2024 und dem Jahrgang, welches ich in der
# Konsole eingebe


# TASK 4: Es gibt ein Spiel welches man ab 12 Personen spielen kann. Ich möchte ein vereinfachtes Programm schreiben,
# welches man die Anzahl der teilnehmenden Spieler eintippt und dann True oder False zurückgegeben bekommt.
# Bei der Input-function soll der Organisator aufgefordert werden, die Anzahl der Spieler einzugeben.
current_players = 12
numbers_of_players = int(input("Please enter the numbers of the player: "))
print(current_players + numbers_of_players >= 12)


# TASK 5: Programmiere einen BMI-Rechner. Ein BMI-Rechner berechnet anhand gewisser Werte, die vom Nutzer abgefragt
# werden, dessen BMI. Schreibe ein Programm, welches alle für die BMI-Berechnung notwendigen Daten einliest,
# anschließend die entsprechende Berechnung durchführt und daraufhin das Ergebnis auf der Konsole ausgibt.

weight = float(input("Körpergewicht in Kg eingeben: "))
height = float(input("Körpergröße in Meter eingeben: "))

bmi = weight / (height * height)
# Ich caste die Variable bmi in ein string, da das noch als Zahlenwert vorliegt.
print("Dein BMI ist: " + str(bmi))


# TASK 6: Programm, welches den User auffordert seinen Nutzernamen, Geburtsdatum, Heimatstadt, E-Mail, Geschlecht,
# Alter, Herkunft und Lieblingsfarbe:
UserName = "Ayoub"
Birthday = 25_08_2001

e_mail = "ayoub.programmierwelt@gmail.com"
Geschlecht = "Männlich"
Alter = 22
Herkunft = "Marokko"

user_input = ""

while True:
    user_input = input("Bitte gebe deinen Nutzernamen ein: ")
    if user_input != UserName:
        continue
    user_input = int(input("Bitte gib dein Geburtsdatum ein: "))
    if user_input != Birthday:
        continue
    user_input = input("Bitte gib deine Heimatstadt ein: ")
    if user_input != "Frankfurt":
        continue
    user_input = input("Danke Ayoub, Gib nun deine E-Mail ein: ")
    if user_input != e_mail:
        continue
    user_input = input("Gib nun dein Geschlecht ein: ")
    if user_input != Geschlecht:
        continue
    user_input = int(input("Gib dein Alter ein: "))
    if user_input != Alter:
        continue
    user_input = input("Bitte gib dein Herkunftsland ein: ")
    if user_input != Herkunft:
        continue
    user_input = input("Bitte gebe deine Lieblingsfarbe ein: ")
    if user_input == "Blue":
        break

print("Du wurdest erfolgreich eingeloggt...")


# TASK 7: Ein Programm, in welchem der Nutzer aufgefordert wird, sein Passwort, Geburtsdatum, Herkunftsland
# und Geschlecht einzugeben, um eingeloggt zu werden
passwort3 = "book"
Geburtsdatum = 25_08_2001
Herkunftsland = "Morocco"
user_input = ""

while user_input != passwort3:
    user_input = input("Bitte gebe das korrekte Passwort ein: ")
    if user_input != passwort3:
        print("Das Passwort ist falsch! Bitte probiere es erneut!")
        continue
    elif user_input == passwort3:
        print("Das Passwort ist richtig!")
    user_input = int(input("Gebe nun bitte dein Geburtsdatum ein: "))
    if user_input != Geburtsdatum:
        print("Fehler! Bitte versuche es erneut!")
        continue
    elif user_input == Geburtsdatum:
        print("Dein Geburtsdatum ist richtig!")
    user_input = input("Bitte gebe dein Herkunftsland ein: ")
    if user_input != Herkunftsland:
        print("Deine Angabe ist falsch!")
        continue
    elif user_input == Herkunftsland:
        print("Deine Angabe ist richtig!")
    user_input = input("Bitte gebe dein Geschlecht ein: ")
    if user_input != "Male":
        print("Deine Angabe ist falsch! Versuche es erneut!")
        continue
    elif user_input == "Male":
        print("All deine Daten stimmen überein!")
        break
print("Du wurdest erfolgreich eingeloggt...")


# TASK 8: Ein Programm, welches die Zahlen von 1 bis 100 auf der Konsole ausgibt. Jede Zahl soll dabei in einer
# seperaten Zeile ausgegeben werden.
# Nun gilt es das Programm noch etwas zu erweitern. Und zwar sollst du jede Zahl, die durch 3 teilbar ist, durch den
# Satz "teilbar durch 3" ersetzen. Jede Zahl, die durch 4 teilbar ist, soll durch den Satz "teilbar durch 4" ersetzt
# werden. Jetzt wird es einige Zahlen geben, die sowohl durch 3 als auch durch 4 teilbar sind (z.B. die 12).
# Bei diesen Zahlen soll dann "teilbar surch 3 und 4" ausgegeben werden.

for numbers in range(1, 101):
    if (numbers % 3) == 0 and (numbers % 4) == 0:  # Diese Abfrage muss als erstes stehen.
        print("teilbar durch 3 und 4.")
    elif (numbers % 3) == 0:
        print("teilbar durch 3.")
    elif (numbers % 4) == 0:
        print("teilbar durch 4.")
    else:
        print(numbers)


# In dieser Aufgabe sollst du einen einfachen Taschenrechner programmieren. Zunächst soll der Nutzer dazu aufgefordert
# werden, zwei beliebige Zahlen in das Programm einzulesen.
# Danach soll der Nutzer mit einer dritten Eingabe entscheiden, welche Operation auf diesen beiden zuvor eingelesenen
# Zahlen ausgeführt werden soll. Dabei soll der Nutzer die Möglichkeit haben, die beiden Zahlen miteinander zu addieren,
# zu subtrahieren, zu dividieren oder zu multiplizieren.
# Je nachdem für welche Operation sich der Nutzer entscheidet, soll dann das entsprechende Ergebnis auf der Konsole
# ausgegeben werden.

number1 = float(input("Gebe die erste Zahl ein: "))
number2 = float(input("Gebe die zweite Zahl ein: "))
operation = input("Welche Operation (+, -, *, /) soll durchgeführt werden: ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("Ungültige Operation...")
