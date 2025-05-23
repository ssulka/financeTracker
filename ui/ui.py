import tkinter as tk
from tkinter import messagebox

class FinanceTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        # Labels and Entry fields
        tk.Label(root, text="Description:").grid(row=0, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(root, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(root, width=30)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Transaction list
        self.transactions = []

    def add_transaction(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if not description or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        self.transactions.append({"description": description, "amount": amount})
        messagebox.showinfo("Success", "Transaction added successfully!")
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def view_transactions(self):
        if not self.transactions:
            messagebox.showinfo("Transactions", "No transactions to display.")
            return

        transactions_str = "\n".join(
            [f"{t['description']}: ${t['amount']:.2f}" for t in self.transactions]
        )
        messagebox.showinfo("Transactions", transactions_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerUI(root)
    root.mainloop()