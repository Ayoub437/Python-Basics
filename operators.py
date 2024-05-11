# An important note: Der Zuweisungsoperator (=) arbeitet immer von rechts nach links.

# Example: Der Operant rechts wird immer dem Operand links zugewiesen.
result1 = 30

# Der komplexe Ausdruck rechts wird zunächst ausgewertet, dann kommt ein Ergebnis raus
# und wird dann dieser Variable zugewiesen.
result2 = (30 + 3) * 3


# Arithmetic operators
# That is integer division (Division ohne Rest).
print(13 // 3)  # In the console is printed 4.

# Modulo operator (Rest der nach Division übrig bleibt)
print(32 % 3)  # In console is printed 2.

# Exponentation
print(3 ** 3)  # That means 3 hoch 3.


variable1 = 3
variable1 = variable1 + 10
print(variable1)

# Defining variables
variable2 = 6
variable3 = 7
variable4 = 3 + 30

# Kombinierter Zuweisungsoperator/ Assignment operator
# When do I use that? A variable has stored a value, I want to execute an
# operation on that value and store the new value in the same variable.
# In variable1 is stored the "Ausdruck" variable1 + 10. Variable1 is already defined
variable1 += 10
print(variable1)

variable2 += 14
print(variable2)

variable3 += 9
print(variable3)

variable4 += 3
print(variable4)

# Vergleichsoperatoren/ Comparison
# Data type named bool
print(2 < 4)  # In console is printed True
print(2 != 3)  # True
print(10 == 10)  # True
print(4 == 5)  # False

print(type(3 >= 1))


# Logical operators
# Why do I need that type of operator? To relate several comparisons to each other/
# Um mehrere Vergleiche miteinander in Beziehung zu setzen
# These are expressions(= Ausdrücke) and that´s why you get
# a truth value(=Wahrheitswert) like True or False.
# In that logical or case, if just one of these expressions
# is True, the logical or is going to be True as well.
# And if both expressions are True, same result
# "or" => logisches ODER       Beispiel: (a < b) or (c == d)
# "and" => logisches UND       Beispiel: (a < b) and (c == d)
# If the claim is True, the logical not is going to be False.
# "not" => logisches NICHT     Beispiel: not b


# Bitwise operators/ Bitweise Operatoren
# These operators always relates to binary numbers(= binäre Zahlen) of dual system.
# The dual system represents just values with 0 and 1.
# Every value from decimal system like 8 or 19 is changeable to 0 and 1 in dual system.
# The decimal number of 010101 is 21.
# Dual system is well suited(=gut geeignet) for systems with just two states(=Zustände). For example, on and off.
# An example, I translate a decimal number to a binary number.
# Dualsystem of 6: 0000 0110
# Every binary number is moved to the left at 1./ Alle Zahlen werden um eins nach links verschoben.
print(6 << 1)
# Result of that is 12. Because I have 6 and want to move it to left.
# Binary result is 0000 1100.

# Another example
# 0000 0111 that is number 7
print(7 << 1)  # 0000 0111

# Another example
# 1010 that is 10.
print(10 << 1)  # 10100 and console is 20

# Another example
# 11110 that is 30
print(30 << 1)
# is 11110 and Console is 60

# Now, I want all bits to right.
print(40 >> 1)  # 0001 0100
# Console: 20

print(6 >> 1)
# Console is 3 and is binary 11


# "AND"-operator:
# individual bits is set to 0, while the other bits stay unchangeable/ Einzelne Bits werden auf 0 gesetzt.
# All Bits that are set to 0 in the mask, are set to 0. / Alle Bits die in der Maske auf 1 sind, werden auf 1 gesetzt
# All bits that are set to 1 in the mask remain unchanged.
# Here I also use hexadecimal numbers.
# Example:
print(6 & 0xFD)  # Console: 4

print(0xB & 0xCD)  # Console: 9

print(8 & 0xCD)  # Console: 8

print(4 & 0xDB)  # Console: 0


# "OR"-operator:
# Einzelne bits auf 1 setzen, während die anderen Bits unverändert bleiben
# Alle Bits die in der Maske 1 sind, werden auf 1 gesetzt
# Alle Bits die in der Maske auf 0 sind, bleiben unverändert.
# Example:
print(6 | 0x01)  # "|" => That is the "OR"-operator.



# Exklusiv-ODER-Operator:
# Bits werden invertiert.
# Funktion der Maske: Alle Bits die in der Maske "1" sind, werden invertiert.
# Alle Bits die in der Maske auf "0" sind, bleiben unverändert.
# Example:
print(8 ^ 0xDB)  # Console: 211
