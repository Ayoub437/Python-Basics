# Today, I learn the type-function.
# That function helps to determine=(ermitteln) the data type.

# First, I have assigned an input-function to a variable.
laptop1 = input("How much does it cost? Cost: ")
laptop2 = input("How much did it cost? cost: ")

# Inside the parentheses, I need to put the value from which I want to determine the
# data type.
# The value is determined, but not printed in the console.
type(laptop2)  # Here I choose that value.


# Another example, but here I print the data type in console by using print-function.
Inventor = input("Who invent the first computer? Name: ")
Programmer = input("Who was the first programmer? Name: ")
print(type(Programmer))  # Here I determine and print the data type of that value.

# Same exercise
Family_frankfurt = input("Is it a big family? Answer: ")
Family_wiesbaden = input("Is it a small family? Answer: ")
# Now I determine and print the data type
print(type(Family_wiesbaden))

# Very important note:
# The input-function can take any kind of value, but that value is always stored
# as a string.


# Exercises without the input-function.
Table = 22  # I defined the variable
print(Table)  # I print the variable in the console.
print(type(Table))  # Here I determine and print the data type of that value.

Houses = 34.34
print(Houses)
print(type(Houses))

# Same exercise
Table = "Big"
print(type(Table))

window = "small"
print(type(window))
