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
