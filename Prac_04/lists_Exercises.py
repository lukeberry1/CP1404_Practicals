# def Main():
#     numbers = []
#     for i in range(5):
#         user_input= int(input("Number:"))
#         numbers.append(user_input)
#     outputs(numbers)
#
#
#
# def outputs(numbers):
#     print("The first numebr is ", numbers[0])
#     print("The last number is ", numbers[-1])
#     print("The smallest number is ", min(numbers))
#     print("The largest number is", max(numbers))
#     print("The average for the numbers is", sum(numbers) / len(numbers))
#
# Main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter Password:")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")

