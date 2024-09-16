import pandas as pd
import numpy as np

class BankAccount:
    def __init__(self, account_number, interest_rate):
        self.account_number = account_number
        self.interest_rate = interest_rate  
        self.transactions = {month: [] for month in range(1, 7)}  

    
    def add_transaction(self, month, amount):
        if month in self.transactions:
            self.transactions[month].append(amount)
        else:
            print(f"Invalid month {month}. Only 1-6 are valid.")

    def find_minimum_balance(self):
        min_balances = {}
        balance = 0

        for month in range(1, 7):
            monthly_transactions = self.transactions[month]
            monthly_balances = [balance + sum(monthly_transactions[:i + 1]) for i in range(len(monthly_transactions))]
            if monthly_balances:
                min_balances[month] = min(monthly_balances)
                balance = monthly_balances[-1]  
            else:
                min_balances[month] = balance  

        return min_balances

    def calculate_interest(self):
        min_balances = self.find_minimum_balance()

        total_min_balance = sum(min_balances.values())

        yearly_interest = total_min_balance * self.interest_rate
        monthly_interest = yearly_interest / 12

        six_month_interest = monthly_interest * 6

        return six_month_interest, min_balances

    def generate_transaction_summary(self):
        max_len = max(len(transactions) for transactions in self.transactions.values())

        padded_transactions = {
            month: transactions + [np.nan] * (max_len - len(transactions)) 
            for month, transactions in self.transactions.items()
        }

        summary = pd.DataFrame(padded_transactions)
        summary.index.name = 'Transaction_Index'
        return summary.T  

account = BankAccount(account_number="123456789", interest_rate=0.05)  # 5% annual interest

account.add_transaction(1, 1000)
account.add_transaction(1, -200)
account.add_transaction(1, 300)
account.add_transaction(2, 1500)
account.add_transaction(2, -500)
account.add_transaction(3, 100)
account.add_transaction(3, -50)
account.add_transaction(4, 1200)
account.add_transaction(4, -300)
account.add_transaction(5, 400)
account.add_transaction(5, -100)
account.add_transaction(6, 700)

transaction_summary = account.generate_transaction_summary()

six_month_interest, min_balances = account.calculate_interest()

transaction_summary, six_month_interest, min_balances