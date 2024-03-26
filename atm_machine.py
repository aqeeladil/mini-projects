class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        # print(id(self))
        self.menu()

    def menu(self):
        user_menu = int(input('''
                           Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           '''))
        if user_menu == 1:
            self.create_pin()
        elif user_menu == 2:
            self.deposit()
        elif user_menu == 3:
            self.withdraw()
        elif user_menu == 4:
            self.check_balance()
        else:
            print('bye')
        
    def create_pin(self):
        self.pin = input('Create your pin: ')
        print('PIN set successfully')
        self.menu()

    def deposit(self):
        temp = input('Enter the pin')
        if (temp == self.pin):
            amount = int(input('Enter the amount'))
            self.balance = self.balance + amount
            print('Deposited successfully')
        else:
            print('Please eneter valid password')
        self.menu()

    def withdraw(self):
        temp = input('Enter the pin')
        if (temp == self.pin):
            amount = int(input('Enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Withdrawal successful')
            else:
                print('Insufficient Balance')
        else:
            print('Enter valid password')
        self.menu()

    def check_balance(self):
        temp = input('Enter the pin')
        if temp == self.pin:
            print(f'Current balance: {self.balance}')
        else:
            print('Enter valid password')
        self.menu()


meezan = Atm()

