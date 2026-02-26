#Write a program asking the user for a list of their monthly expenses. When asking the user for their expenses,
#ask for the type of expense and the amount. Use the reduce method to analyze the expenses and display the total
#expense, the highest expense and the lowest expense. Label what the highest and lowest expense is.
from functools import reduce
import sys

def main():
    #running two lists parallel because it's easier for the purposes of this assignment
    names = []
    costs = []

    #initial explanation of user prompt
    print('Hi, I can take your expenses and find your highest, lowest, and total expenses.')

    #making the user predefine the list length, so I don't have to ask every time he enters an expense
    while True:
        try:
            numbof = int(input('How many expenses do you have? '))
            if numbof < 0:
                raise ValueError
            elif numbof == 0:
                sys.exit('you have no expenses, good for you.')
            break
        except ValueError:
            print('Please enter a positive integer.')
    while numbof > 0:
        #user input for the description for each expense ie. corresponding element from name list to cost list
        names.append(input('what type of expense do you have? '))
        #Value error exception for smartasses that don't want to enter a number
        while True:
            try:
                #user input for cost elements
                costs.append(float(input("How much is your expense? $")))
                break
            except ValueError:
                print('Please enter a number.')
        numbof -= 1

    #lambda functions for total, max, and min
    t = reduce(lambda x, y: x + y, costs)
    b = reduce(lambda x, y: x if x > y else y, costs)
    s = reduce(lambda x, y: x if x < y else y, costs)

    #list test
    #print(names)
    #print(costs)
    #print(t)
    #print(b)
    #print(s)

    #finds the index of the min/max of the cost list and plugs it into the names list for the name of the expense
    print('Your total expenses are: $', t)
    print('Your highest expense is: ', names[costs.index(b)], ': $', b)
    print('Your lowest expense is: ', names[costs.index(s)], ': $', s)

main()