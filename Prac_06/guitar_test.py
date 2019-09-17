from Prac_06.guitar import Guitar

Guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print("{} get_age() - Expected 97. Got {}".format(Guitar.name, Guitar.get_age()))
print("{} get_age() - Expected True. Got {}".format(Guitar.name, Guitar.is_vintage()))
