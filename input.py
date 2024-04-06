# In this file I learn the input-function

# Through these parentheses the input-funtion will be executed.
# The input-function stops the other print command.
# As soon as the input command is executed, the program stops and wait for an input from the user in the console.
# If I assign the input-function to a variable, then I use that variable in the print-command in the next line.
# If I do that, The value of that variable, in this case input-function, is to be printed in the console.
# Die Eingabe tätige ich in der Konsole.
print("Eating")
time = input()
print("I ate my lunch " + time)
input()

print("Now I am talking about me.")
name = input()
print("My name is " + name)
input()

print("To do list")
today = input()
print("The things I wanted to do is done " + today)
input()

print("Hello")
city = input()
print("I just wanna tell you " + city)
input()

# Another kind of input-function
# The string inside the input-function will appear in the console.
# I can write something next to the string in the console and the writing will be in green.
# After I did it, it will be emitted=(ausgegeben) in the next line in the console.
subject = input("Please enter your name:")
print(subject)

# More exercises with input function
print("Hello dear class")
presentation = input()
print("Today I will give a presentation " + presentation)
input()

# Sample tasks
print("I wanna make a party")
drinks = input()
print("This week I bought " + drinks)
input()

print("New line")
today = input()
print("Talking about the things I wanna do today " + today)
input()

print("Universe")
universe = input()
print("The universe is very " + universe)

value1 = input("Gebe die erste Zahl ein: ")
value2 = input("Gebe die zweite Zahl ein: ")
# If I use the print-function for these variables, they will be printed as well.
# They will stand next to each in console, but with a distance.
print(value1, value2)
# The values which I give in the console to these values of these variables will
# stand next to each other in console.
# They are not calculated against each other.
print(value1 + value2)

# Same exercise
House1 = input("Give the city of your current residence: ")
House2 = input("Give the city of your former residence: ")
print(House1, House2)  # What I write in console will stand next to each other, but
# with distance.
print(House1 + House2)  # Without distance.

# Same exercise
cost1 = input("Please write here the cost of your apartment: ")
cost2 = input("Please tell us the cost of the dinner: ")
