# Learning the basic functionalities of list.

# Figuring out the length of a list/ Writing the number of the values within a list.
# How do I do that? By using the function named len.
Jobs = ["Computer scientist", 34, "Police-officer", 20]
print(len(Jobs))

Fingers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Residents = [3e6, 4e5, 3e5]
print(len(Fingers))
print(len(Residents))


# Here I add a new value to an already existing list, but always at the end.
# How do I do that? By using the append-function.
# That function is just used in the context of lists, that is why it works
# different as the other functions.
stones = ["Big", "small", 23, 40]
# To use it, I write the variable and then the append-funtion.
stones.append(30)
print(stones)

# Another way to add a new value to an already existing
# list is to use the insert-function.
# The difference to that function and the "append" is that
# in insert-function I can exactly write in which index it should be added.
Names = ["Marie", "Janek", "Jonas", "Bilal"]
# The first Parameter is the index where it shall add.
# Second parameter is the new value.
Names.insert(3, "Mohammed")
print(Names)

# Same exercise
Handys = [12, 40, 1, 4, 90]
Handys.insert(0, 23)
print(Handys)

# Same exercise
Numbers = [12, 34, 56, 67, 100]
Numbers.insert(2, 50)
print(Numbers)

rent = [20, "Big", "Small", 40]
rent.insert(1, 23)
print(rent)

# Append-function
Costs = [23, 40, 10, 50, 90]
Costs.append(100)
print(Costs)

# New function. Popp-function. That function always
# deletes the last element of a list.
vacations = ["morocco", 33, "USA", 22]
vacations.pop()
vacations.pop()
print(vacations)


# The "remove-function" deletes a certain value/element of my list.
# How? By writing the value inside the remove-function that shall be deleted.
nations = ["austria", "USA", "Canada", "china"]
nations.remove("USA")
print(nations)

countries = ["South-africa", "russia", "australia", "egypt"]
countries.remove("russia")
print(countries)
