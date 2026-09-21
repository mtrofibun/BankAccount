from bank_account import Bank
class Checking(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance,account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

    def transfer_limit():
        pass