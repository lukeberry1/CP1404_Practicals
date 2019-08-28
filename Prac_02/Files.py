NAME = "Name File"
out_file = open("NAME.txt", "w")
Name = input("Enter your Name")
print(Name, file=out_file)
out_file.close()

in_file = open("NAME.txt", "r")
print("your name is ", in_file.readline())
in_file.close()

Numbers = "Number list"
in_file = open("Numbers.txt", "r")
result = int(in_file.readline()) + int(in_file.readline())
in_file.close()
print(result)

number_total = "Total Numbers"
in_file = open("number_total.txt", "r")
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
