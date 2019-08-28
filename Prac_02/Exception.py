try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""When will a ValueError occur? when the value isn't an integer eg. string or float
When will a ZeroDivisionError occur? what you enter 0 as the denominator 
Could you change the code to avoid the possibility of a ZeroDivisionError? yes use a while loop while numerator == 0"""
