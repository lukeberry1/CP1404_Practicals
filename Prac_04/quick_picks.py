import random

Number_per_line = 6
Max_number = 45
Min_number = 1

number_of_quick_picks = int(input("Enter the number of quick picks:"))

for j in range(number_of_quick_picks):
    quick_pick_list = []
    for i in range(Number_per_line):
        number = random.randint(Min_number, Max_number)
        while number in quick_pick_list:
            number = random.randint(Min_number, Max_number)
        quick_pick_list.append(number)
        quick_pick_list.sort()
    print(quick_pick_list)
