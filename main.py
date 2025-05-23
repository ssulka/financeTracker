import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# File to store financial data
DATA_FILE = "finance_data.json"

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new transaction
def add_transaction(amount, category, description=""):
    data = load_data()
    transaction = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(transaction)
    save_data(data)
    print("Transaction added successfully!")

# View all transactions in CLI
def view_transactions():
    data = load_data()
    if not data:
        print("No transactions found.")
        return
    for transaction in data:
        print(transaction)

# Open GUI
def open_ui():
    def add_transaction_ui():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            description = description_entry.get()
            if not category:
                raise ValueError("Category cannot be empty.")
            add_transaction(amount, category, description)
            messagebox.showinfo("Success", "Transaction added successfully!")
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def view_transactions_ui():
        transactions = load_data()
        if not transactions:
            messagebox.showinfo("Transactions", "No transactions found.")
            return
        transactions_str = "\n".join(
            [f"{t['date']} - {t['category']} - {t['amount']} - {t['description']}" for t in transactions]
        )
        messagebox.showinfo("Transactions", transactions_str)

    root = tk.Tk()
    root.title("Finance Tracker")

    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
    category_entry = tk.Entry(root)
    category_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Description:").grid(row=2, column=0, padx=5, pady=5)
    description_entry = tk.Entry(root)
    description_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(root, text="Add Transaction", command=add_transaction_ui).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="View Transactions", command=view_transactions_ui).grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

# Console-based main menu
def main():
    while True:
        print("\nFinance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                add_transaction(amount, category, description)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    mode = input("Choose mode (ui / cli): ").strip().lower()
    if mode == "ui":
        open_ui()
    else:
        main()
