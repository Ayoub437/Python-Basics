# Using the type-casting-function
# What does that function? I can convert a data type to another data type.
# By using type-casting, I can calculate integer-values against each other in console
# although using input-function.

# Remember, Input-function always stores the values as strings. That is why the
# integers in console have been chained together, instead of calculate against each other.

# Exercise with input-function
value3 = input("How old are you? Age: ")
value4 = input("How old is he? Age: ")
print(int(value3) + int(value4))

value5 = input("How many labours work in this company? ")
value6 = input("How much percent did you do? ")
print(int(value5) + int(value6))

example_1 = input("Line 18: Say me your age: ")
example_2 = input("How many people are here? ")
print(int(example_1) * int(example_2))

product_1 = input("How much does it cost? ")
product_2 = input("How much does the banana cost? ")
print("What is the rest?")
print(float(product_1) - float(product_2))

learn_1 = input("What did you learn today? ")
learn_2 = input("How did you learn? ")
print(str(learn_1) + str(learn_2))  # In that case, to add the data type before the variable is unnecessary,
# because the values inside the input-functions are always stored as a string.

Window_12 = input("Line 32: How much did you pay? ")
Window_11 = input("How much did you pay? ")
print(float(Window_12) + int(Window_11))
