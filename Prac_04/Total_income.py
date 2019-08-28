"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of Number_of_months."""
    incomes = []
    Number_of_months = int(input("How many months? "))

    for Number_of_months in range(1, Number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(Number_of_months)))
        incomes.append(income)
    result = print_income(Number_of_months, incomes)

def print_income(Number_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for Number_of_months in range(1, Number_of_months + 1):
        income = incomes[Number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(Number_of_months, income, total))


main()