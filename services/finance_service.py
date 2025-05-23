class FinanceService:
    def __init__(self):
        # Initialize an in-memory list to store transactions
        self.transactions = []

    def add_transaction(self, amount, category, date, description=""):
        transaction = {
            "amount": amount,
            "category": category,
            "date": date,
            "description": description,
        }
        self.transactions.append(transaction)

    def get_transactions(self, start_date=None, end_date=None):
        if not start_date and not end_date:
            return self.transactions

        filtered_transactions = []
        for transaction in self.transactions:
            if start_date and transaction["date"] < start_date:
                continue
            if end_date and transaction["date"] > end_date:
                continue
            filtered_transactions.append(transaction)
        return filtered_transactions

    def calculate_total_expenses(self, start_date=None, end_date=None):
        transactions = self.get_transactions(start_date, end_date)
        total_expenses = sum(
            transaction["amount"] for transaction in transactions if transaction["amount"] < 0
        )
        return abs(total_expenses)

    def calculate_total_income(self, start_date=None, end_date=None):
        transactions = self.get_transactions(start_date, end_date)
        total_income = sum(
            transaction["amount"] for transaction in transactions if transaction["amount"] > 0
        )
        return total_income