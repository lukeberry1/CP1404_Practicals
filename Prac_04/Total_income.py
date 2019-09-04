"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for number_of_months in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(number_of_months)))
        incomes.append(income)
    print_income(number_of_months, incomes)


def print_income(number_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, number_of_months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))


main()
