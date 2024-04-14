# Task 1: Write a program which you can use to track people.
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


# Task 2: Extend this program so that the user is asked to enter the value 0,
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
