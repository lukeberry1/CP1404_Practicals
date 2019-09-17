from Prac_06.guitar import Guitar


guitars = []
name = input("name:")
while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print("{} ({}) : {} added".format(name, year, cost))
    name = input("name:")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")

for i, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
