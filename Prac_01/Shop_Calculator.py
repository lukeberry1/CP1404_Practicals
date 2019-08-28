Number_of_items = int(input("Number of Items:"))
Total = 0
while Number_of_items < 0:
    print("Invalid number of items!")
    Number_of_items = int(input("Number of Items:"))

if Number_of_items > 0:
    for i in range(Number_of_items):
        Prices = float(input("Price of Item:"))
        Total += Prices

if Total >= 100:
    Total = Total - (0.1 * Total)

print("Total Price for {} items is: ${:.2f}".format(Number_of_items, Total))
