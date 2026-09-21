class Bank:
    title = "Bank"

    # init method
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float, account_number:int, routing_number:int):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number
    # methods
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.current_balance += amount
        print(f"New balance is ${self.current_balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        # error validation
        if self.current_balance - amount < self.minimum_balance:
            print("Withdraw not completed : Balance is less than minimum balance")
        else:
            self.current_balance -= amount
            print(f"New balance is ${self.current_balance:.2f}")

        def get_routing_number(self):
            return self.routing_number
    
    def print_customer_info(self):
        print(f"Bank: {self.title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current balance: ${self.current_balance:.2f}")
        print(f"Minimum balance: {self.minimum_balance:.2f}")



john = Bank("John Smith", 90.15, 30.00)
jane = Bank("Jane Smith", 70.15, 10.00)

jane.withdraw()
john.deposit()