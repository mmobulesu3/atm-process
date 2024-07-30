class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []
        self.name = None  # Initialize name attribute

    def display_menu(self):
        print("\nWelcome to the ATM")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")

    def check_balance(self):
        print(f"\nHello, {self.name}! Your current balance is {self.balance}:RUPEES")

    def withdraw_cash(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"\nHello, {self.name}! You have withdrawn {amount}:RUPEES. Remaining balance is {self.balance}:RUPEES")
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("\nHello, {self.name}! Insufficient funds or invalid amount.")

    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nHello, {self.name}! You have deposited ${amount}. New balance is {self.balance}:RUPEES ")
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("\nHello, {self.name}! Invalid amount.")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("\nHello, {self.name}! PIN changed successfully.")
        else:
            print("\nHello, {self.name}! Incorrect PIN. PIN change failed.")

    def display_transaction_history(self):
        print(f"\nHello, {self.name}! Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    @staticmethod
    def create_pin():
        while True:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                return new_pin
            else:
                print("PINs do not match. Please try again.")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw_cash(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.deposit_cash(amount)
            elif choice == '4':
                old_pin = input("Enter current PIN: ")
                new_pin = self.create_pin()
                self.change_pin(old_pin, new_pin)
            elif choice == '5':
                self.display_transaction_history()
            elif choice == '6':
                print(f"Thank you for using the ATM, {self.name}!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

# ATM usage
if __name__ == "__main__":
    initial_balance = 25000  # Initial balance
    pin = "2003"  # Initial PIN

    atm = ATM(initial_balance, pin)

    while True:
        print('Hello user')
        ch = input('Please insert your card (yes): ')

        if ch.lower() == 'yes':
            while True:
                new_user = input('Are you a new user? (yes/no): ').lower()
                if new_user == 'yes':
                    atm.name = input('Enter your name: ')
                    pin = atm.create_pin()
                    print(f'Hello, {atm.name}! Your new PIN is: {pin}')
                    break
                elif new_user == 'no':
                    p = input('Enter your PIN number: ')
                    if p == pin:
                        atm.name = input('Enter your name: ')
                        print(f'Hello, {atm.name}! PIN accepted. Welcome!')
                        break
                    else:
                        print('Invalid PIN. Please try again.')
                else:
                    print('Invalid input. Please enter yes or no.')

            atm.start()

            restart = input("Do you want to perform another transaction? (yes/no): ").lower()
            if restart != 'yes':
                print(f'Thank you, {atm.name}. Have a nice day!')
                break
        else:
            print('Thank you. Have a nice day!')
            break
