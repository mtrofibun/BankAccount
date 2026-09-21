from bank_account import Bank
class Savings(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.account_number = account_number
        self.routing_number = routing_number