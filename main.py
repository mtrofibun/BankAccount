from checking_account import Checking
from routing_account import Savings

# Use case #1 user opens a savings account, gets interest, deposits, checks information

savings1 = Savings("John Smith",130,30,12345,54321,interest_rate=0.5)
savings2 = Savings("Jane Smith",150,50, 54321,12345,interest_rate=0.4)

savings1.print_customer_info()
savings1.interest()
savings1.deposit(50)
savings1.print_customer_info()

savings2.print_customer_info()
savings2.interest()
savings2.deposit(10)
savings2.print_customer_info()

# Use case 2 - user creates a checking account, withdrawals past minimum, deposits then transfers to another account
account1 = Checking("John Smith",50,50,98765,56789,100)
account2 = Checking("Jane Smith",100,50,12345,544321,100)
account1.withdraw(90)
account1.deposit(100)
account1.transfer(90,account2)
account2.print_customer_info()