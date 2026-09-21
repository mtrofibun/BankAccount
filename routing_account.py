from bank_account import Bank
class Savings(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number,interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def interest(self):
        interest_value = self.current_balance * self.interest
        self.current_balance += interest_value
        print(f"Interest gained : ${interest_value:.2f}\n New balance : ${self.current_balance:.2f}")