import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
    print("\n--- Transactions ---")
    for t in data:
        print(f"{t['date']} | {t['category']:12} | €{t['amount']:7.2f} | {t['description']}")

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
            refresh_table()
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def refresh_table():
        for row in tree.get_children():
            tree.delete(row)
        total = 0
        for t in load_data():
            tree.insert("", "end", values=(t['date'], t['category'], f"€{t['amount']:.2f}", t['description']))
            total += float(t['amount'])
        total_label.config(text=f"Total Expenses: €{total:.2f}")

    root = tk.Tk()
    root.title("Finance Tracker")

    # Inputs
    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    category_entry = tk.Entry(root)
    category_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    description_entry = tk.Entry(root)
    description_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(root, text="Add Transaction", command=add_transaction_ui).grid(row=3, column=0, columnspan=2, pady=10)

    # Table for transactions
    columns = ("date", "category", "amount", "description")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120 if col != "description" else 200)
    tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Total expenses label
    total_label = tk.Label(root, text="Total Expenses: €0.00", font=("Arial", 12, "bold"))
    total_label.grid(row=5, column=0, columnspan=2, pady=(5, 15))

    refresh_table()
    root.mainloop()


# Console-based main menu
def main():
    print("Welcome to the Finance Tracker (CLI mode)\n")

    while True:
        print("\n===== MENU =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount (e.g. 19.99): "))
                category = input("Enter category (e.g. Groceries): ").strip()
                if not category:
                    print("Category cannot be empty.")
                    continue
                description = input("Enter description (optional): ").strip()
                add_transaction(amount, category, description)
            except ValueError:
                print(" Invalid amount. Please enter a numeric value.")
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            print("Goodbye! 💸")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")

# Entry point
if __name__ == "__main__":
    mode = input("Choose mode (ui / cli): ").strip().lower()
    if mode == "ui":
        open_ui()
    else:
        main()
