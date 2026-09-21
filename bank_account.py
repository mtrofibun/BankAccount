class Bank:
    title = "Bank"

    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float, account_number:int, routing_number:int):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.current_balance += amount
        print(f"New balance is ${self.current_balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if self.current_balance - amount < self.minimum_balance:
            print("Amount exceeds current balance")
        else:
            self.current_balance -= amount
            print(f"New balance is ${self.current_balance:.2f}")

    def print_customer_info(self):
        print(f"{self.title}: {self.customer_name}")
        print(f"Current balance: ${self.current_balance:.2f}")



john = Bank("John Smith", 90.15, 30.00)
jane = Bank("Jane Smith", 70.15, 10.00)

jane.withdraw()
john.deposit()