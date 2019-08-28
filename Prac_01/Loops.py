for i in range(1, 21, 2):
    print(i, end=' ')


for i in range(0, 101, 10):
    print(i, end=' ')

for i in range(20, 0, -1):
    print(i, end=' ')

stars = int(input("Number of stars:"))
for i in range(stars):
    print("*", end=' ')

for i in range(stars):
    print((i+1) * "*")
