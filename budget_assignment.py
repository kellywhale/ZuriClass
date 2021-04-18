class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit_funds(self):
        deposit_amount = int(input("How much do you want to add to your %s category? \n" % self.name))
        self.balance = (self.balance + deposit_amount)
        print('%s, your new balance for %s is ' % (username, self.name))
        print(self.balance)

    def withdraw_funds(self):
        withdraw_amount = int(input('How much do you want to withdraw from your %s category? \n' % self.name))
        self.balance = (self.balance - withdraw_amount)
        print('%s, your new balance for %s is ' % (username, self.name))
        print(self.balance)

    def balance_funds(self):
        print("%s, your %s category balance is " % (username, self.name))
        print(self.balance)

    def transfer_funds(self):
        pass


food = Budget('food', 0)
clothing = Budget('clothing', 0)
entertainment = Budget('entertainment', 0)

username = input('What is your name?\n')
print('what do you want to do?')
print('1. Deposit')
print('2. Withdraw')
print('3. Balance')
print('4. Transfer')
selected_option = int(input('Please select an option:'))

if selected_option == 1:
    print('Where do you want to deposit in')
    deposit_category = int(input('1. food 2. Clothing 3. Entertainment \n'))
    if deposit_category == 1:
        food.deposit_funds()
    elif deposit_category == 2:
        clothing.deposit_funds()
    elif deposit_category == 3:
        entertainment.deposit_funds()
    else:
        print('invalid option selected')

elif selected_option == 2:
    print('Where do you want to withdraw from')
    withdraw_category = int(input('1. food 2. Clothing 3. Entertainment \n'))
    if withdraw_category == 1:
        food.withdraw_funds()
    elif withdraw_category == 2:
        clothing.withdraw_funds()
    elif withdraw_category == 3:
        entertainment.withdraw_funds()
    else:
        print('invalid option selected')

elif selected_option == 3:
    print('balance of with Category')
    balance_category = int(input('1. food 2. Clothing 3. Entertainment \n'))
    if balance_category == 1:
        food.balance_funds()
    elif balance_category == 2:
        clothing.balance_funds()
    elif balance_category == 3:
        entertainment.balance_funds()
    else:
        print('invalid option selected')

elif selected_option == 4:
    pass

else:
    print('invalid option selected')
