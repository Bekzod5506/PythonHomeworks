# =========================
# PART 1: FARM MODEL


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def walk(self):
        print(f"{self.name} is walking.")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")


class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_eggs(self):
        print(f"{self.name} laid an egg.")


class Sheep(Animal):
    def make_sound(self):
        print(f"{self.name} says Baa!")

    def shear_wool(self):
        print(f"{self.name} is being sheared for wool.")


def farm_demo():
    print("\n--- FARM DEMO ---")
    cow = Cow("Bella", 5)
    chicken = Chicken("Lily", 2)
    sheep = Sheep("Max", 4)

    animals = [cow, chicken, sheep]

    for animal in animals:
        animal.eat()
        animal.sleep()
        animal.walk()

    cow.make_sound()
    cow.produce_milk()

    chicken.make_sound()
    chicken.lay_eggs()

    sheep.make_sound()
    sheep.shear_wool()


# =========================
# PART 2: BANK APPLICATION


import os


class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(5)

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print("Account created successfully.")
        print(account)

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
        else:
            print(account)

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        account.balance += amount
        self.save_to_file()
        print("Deposit successful.")
        print(account)

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        if amount > account.balance:
            print("Insufficient balance.")
            return

        account.balance -= amount
        self.save_to_file()
        print("Withdrawal successful.")
        print(account)

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                account_number, name, balance = line.strip().split(",")
                self.accounts[account_number] = Account(
                    account_number, name, float(balance)
                )


def bank_menu():
    bank = Bank()

    while True:
        print("\n--- BANK MENU ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, deposit)

            elif choice == "2":
                acc_num = input("Enter account number: ")
                bank.view_account(acc_num)

            elif choice == "3":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                bank.deposit(acc_num, amount)

            elif choice == "4":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(acc_num, amount)

            elif choice == "5":
                print("Exiting application.")
                break

            else:
                print("Invalid option.")

        except ValueError as e:
            print("Error:", e)


# =========================
# MAIN PROGRAM


if __name__ == "__main__":
    farm_demo()
    bank_menu()
