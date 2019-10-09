from Prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Line 6 JTV-59", 2010, 1512.9)
print("{} get_age() - Expected 97. Got {}".format(guitar_1.name, guitar_1.get_age()))
print("{} get_age() - Expected True. Got {}".format(guitar_1.name, guitar_1.is_vintage()))
print("{} get_age() - Expected 9. Got {}".format(another.name, another.get_age()))
print("{} get_age() - Expected False. Got {}".format(another.name, another.is_vintage()))
