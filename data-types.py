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


# Getting access to the list
print(Cars[0])  # The number inside the square brackets refers to
# the index. # In that case, the value "Audi" is printed.

# I can also print several values from different lists at once.
print(ShoppingList[3], Cars[2])


# Some exercises about that
BigCompanies = ["Google", 22, "Facebook", 44, "Mercedes"]
Animes = ["Dragon Ball", "Naruto", "Attack on Titan"]
print(Animes[1], BigCompanies[3])
# printed from the same list.
print(BigCompanies[2], BigCompanies[0])

Tables = ["Big", "small", 30, 2]
Chairs = ["short", "long", 40]
print(Tables[2], Chairs[0])

# Another way to choose certain index is to use minus sign
# At negative (minus), it starts at -1 and not 0
Countries = ["Germany", "France", "England", "Spain"]
Cities = ["Berlin", "Frankfurt", "Wiesbaden"]
print(Countries[-1])  # It starts from the end by using minus. The value "Spain" is printed.
print(Countries[-3], Countries[-4])
print(Cities[-2])

# Here I replace certain values in my list
Fast_Food = ["McDonald", "Dönerladen"]
Fast_Food[0] = "Pizzahut"
print(Fast_Food)

# Same exercise
# You can change a certain value the whole time. Just like that.
Siblings = ["lovingly", "4 sisters", "family"]
Siblings[-1] = "BigFamily"
print(Siblings)
Siblings[-1] = "SmallFamily"
print(Siblings)

# Same exercise
Kids = ["Boy", "Girl", "12-years old", "13-years old"]
Kids[-2] = "9-years old"
print(Kids)
Kids[-1] = "24-years old"
print(Kids)
Kids[-3] = "8-years old"
print(Kids)

# Choose several values of my list at once.
Europe = ["Germany", "Switzerland", "Spain", "France"]
Africa = ["Morocco", "Algeria", "Tunisia", "Togo"]
print(Europe[1:3])  # printing the ranch. The last index 3 is
# excluded. Print: "Switzerland" and "Spain" are printed.

# Now I want all values except the last.
print(Europe[:3])  # Here everything is printed, except the last.
print(Africa[2:])

# Same exercise
Continents = ["Europe", "Africa", "Asia", "North-america"]
print(Continents[:3])
print(Continents[1:])
print(Continents[1:3])

Numbers = [20, 30, 40, 50, 60, 70]
print(Numbers[-2:])  # At minus sign, it is from the end to the start.
print(Numbers[:2])
print(Numbers[:4])  # till the index 4, everything is printed.


# Replacement
Numbers[2] = 200
print(Numbers)


# A good view about lists
Houses = [100, 200, 300, 400, 500, 600, 700]
# If I have double points at the beginning, it means it prints till index 4.
print(Houses[:4])
# Double points at the end, it means it prints from index 4 till the end
print(Houses[4:])
