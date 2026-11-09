#bankacc class contains name, account number, amount, and interest rate. The class has a method that supports
#adjusting interest rate, withdrawing, deipositing, and giving a balance
import math


class BankAcct:
    def __init__(self, name, balance, number, rate):
        self.name = name
        self.balance = balance
        self.number = number
        self.rate = rate

    def adjint(self):
        adj = float(input("enter a new intrest rate: "))
        self.rate = adj

    def deposit(self):
        dep = float(input("How much would you like to deposit into your account: "))
        self.balance += dep

    def withdraw(self):
        wit = float(input("How much would you like to withdraw from your account: "))
        self.balance -= wit

    def show(self):
        print(self.balance)

    def calcinterest(self):
        d = int(input("give me a number of days: "))
        i = d/365
        interest = self.balance * (math.e ** (self.rate * i)) - self.balance
        print("you will owe: ", f"{interest:.2f}", "after ", d, " days")

    def __str__(self):
        return f"Name: '{self.name}'\nBalance: {self.balance}\nAccount number: {self.number}\nInterest rate: {self.rate}"


def test():
    myacc = BankAcct("jason",2754.21, 13324554, .067)
    print(myacc,'\n')
    myacc.adjint()
    print(myacc,'\n')
    myacc.deposit()
    print(myacc,'\n')
    myacc.withdraw()
    print(myacc,'\n')
    myacc.calcinterest()
    myacc.show()

test()