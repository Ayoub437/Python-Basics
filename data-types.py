# Working with basic data-types.

# Here I defined a value, but it changes because I add a new value in the print-function.
# So in the console will be as result 55.
test_variables = 30
print(test_variables + 25)

# Here I just do some exercises about that
number_of_labours = 30
print(number_of_labours - 5)

number_of_frankfurt_citizens = 700000
print(number_of_frankfurt_citizens + 100000)

# I noticed that I can not work with different data types at once.
# If I defined a variable with integer, I can not add a string within the parentheses.
fingers = 10
print(fingers - 5)

president_usa = "Joe Biden"
print(president_usa + " Barack Obama")

Bill = 32.45
print(Bill + 30)

# NOTE: A good thing to know is if I have a number which is too big, an "inf" will appear in my console.
# That "inf" stands for infinity = unendlich
# If in the console is "nan" = not a number. It means it is not calculable = berechenbar

# Now, I do some exercises with the basic data type "list".
# With list, I can store multiple values to a variable.
ShoppingList = ["Tomato", 23, "Jonas", 13, "Frankfurt"]
print(type(ShoppingList))  # Here I try to figure out the data type

# Another list
Cars = ["Audi", "Opel", 30, "Ferrari"]

print(Cars, ShoppingList)  # These 2 lists will be printed.
