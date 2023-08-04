def withdraw(self, amount: float) -> None:  # start of method block
    if self.balance >= amount:  # start of if block
        self.balance -= amount
    # end of if block


# end of method block


def doWithdraw(amount):
    balance = 500

    if balance >= amount:
        print("The amount has been withdrawn")
    print("Thank you for being our customer, have a nice day!")


def deposit(amount):
    balance = 500
    balance += amount
    print(f"The new balance is {balance}")


# The amount has been withdrawn,
# Thank you for being our customer, have a nice day!
doWithdraw(100)

# Thank you for being our customer, have a nice day!
doWithdraw(800)

# The new balance is 750
deposit(250)
