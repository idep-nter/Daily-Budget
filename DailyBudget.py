import datetime
import math

def main():
    """
    Main function starts by determining number of days of the current month and
    then takes necessary data from user.
    If there are any regular expenses it prints them in a structured table.
    Then it subtracts expenses and savings from monthly salary and divides it
    by number of days.
    At the end it prints user's daily budget.
    """
    y = datetime.date.today().year
    m = datetime.date.today().month
    d = days(m, y)
    salary = getSalary()
    currency = getCurrency()
    savings = getSavings()
    expenses = makeExpenses()
    if expenses:
        expensesTable()
        monthlyBudget = math.floor(salary - countTotalExpenses(expenses) -
                                   savings)
    else:
        monthlyBudget = math.floor(salary - savings)

    dailyBudget = math.floor(monthlyBudget / d)
    month = getMonthName()
    print(f'Your daily budget for {month} is: {dailyBudget} {currency}')

def days(m, y):
    """
    Returns number of days based on the current month and year.
    """
    d = 0
    if m == 2 and isLeap(y):
        d = 29
    elif m == 2:
        d = 28
    elif m % 2 == 0:
        d = 30
    else:
        d = 31

    return d

def isLeap(y):
    """
    Determines whether the current year is leap.
    """
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    return False

def getSalary():
    """
    Asks user to enter his salary and checks if it's an integer.
    """
    while True:
        try:
            salary = int(input('Enter your salary: '))
        except ValueError:
                print('Must be a number!')
                continue
        else:
            return salary

def getCurrency():
    """
    Asks user to enter currency and checks if all characters in the string
    are alphabets.
    """
    while True:
        try:
            currency = input('Enter your currency: ')
            if not currency.isalpha():
                raise ValueError
        except ValueError:
            print('Must be only letters!')
            continue
        else:
            return currency

def getSavings():
    """
    Asks user to enter how much he wants to save and checks if it's an integer.
    """
    while True:
        try:
            savings = int(input('How much money do you want to monthly save?: '))
        except ValueError:
                print('Must be a number!')
                continue
        else:
            return savings


def makeExpenses():
    """
    Allows user to enter regular monthly expenses that will be subtracted from
    monthly budget and saves them into a dictionary.
    It also checks correct format of given data.
    """
    expenses = {}
    while True:
        try:
            ex = input('What are your regular monthly expenses(rent, bills etc.)?'
                           '\n*format: expense cost\n*q for quit\n')
            print('\n')
            if ex == 'q':
                break
            ex = ex.split()
            expenses[ex[0]] = int(ex[1])
            continue
        except IndexError or ValueError:
            print('Please enter expenses in given format: expense cost')
            continue
    return expenses

def countTotalExpenses(expenses):
    """
    Takes expenses as a parameter and returns sum of them.
    """
    totalExpenses = 0
    for ex in expenses.values():
        totalExpenses += ex

    return totalExpenses

def expensesTable():
    """
    Prints structured table of all monthly expenses.
    """
    print('=' * 40)
    print('These are you regular monthly expenses:\n')
    for k, v in expenses.items():
        print(f'{k:<15}{v:>10} {currency}')

    totalexpenses = countTotalExpenses(expenses)
    print('-' * 40 + f'\nTotal expenses: {totalexpenses:>10} {currency}')
    print('=' * 40 + '\n')

def getMonthName():
    """
    Returns name of the current month in an alphabetic form.
    """
    date = datetime.datetime.now()
    month = date.strftime("%B")

    return month