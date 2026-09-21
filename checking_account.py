from bank_account import Bank
class Checking(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance,account_number, routing_number,transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
    def transfer(self,amount, user_account):
        if amount > self.transfer_limit:
            print(f"Transfer not completed: amount exceeds transfer limit of ${self.transfer_limit:.2f}")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Transfer not completed: amount would be less than minimum balance")
        else:
            self.current_balance -= amount
            user_account.current_balance += amount 
            print(f"Transfer completed: ${amount:.2f} was transfered to {user_account.customer_name}")