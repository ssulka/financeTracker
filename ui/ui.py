import customtkinter as ctk
from tkinter import messagebox

class FinanceTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("💸 Finance Tracker")
        self.geometry("480x500")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.transactions = []

        # === Heading ===
        self.heading = ctk.CTkLabel(self, text="Finance Tracker", font=ctk.CTkFont(size=24, weight="bold"))
        self.heading.pack(pady=(20, 10))

        # === Entry Frame ===
        entry_frame = ctk.CTkFrame(self)
        entry_frame.pack(pady=10, padx=20, fill="x")

        self.description_entry = ctk.CTkEntry(entry_frame, placeholder_text="Description")
        self.description_entry.pack(pady=10, padx=20, fill="x")

        self.amount_entry = ctk.CTkEntry(entry_frame, placeholder_text="Amount ($)")
        self.amount_entry.pack(pady=(0, 10), padx=20, fill="x")

        self.add_button = ctk.CTkButton(entry_frame, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack(pady=(0, 15), padx=20)

        # === Transactions Frame ===
        transactions_frame = ctk.CTkFrame(self)
        transactions_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.transactions_box = ctk.CTkTextbox(transactions_frame, height=250)
        self.transactions_box.pack(padx=20, pady=10, fill="both", expand=True)
        self.transactions_box.configure(state="disabled")

    def add_transaction(self):
        description = self.description_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not description or not amount:
            messagebox.showerror("Input Error", "Please fill in both fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return

        self.transactions.append({"description": description, "amount": amount})
        self.update_transactions_display()

        self.description_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')

    def update_transactions_display(self):
        self.transactions_box.configure(state="normal")
        self.transactions_box.delete("1.0", "end")
        for t in self.transactions:
            self.transactions_box.insert("end", f"{t['description']}: ${t['amount']:.2f}\n")
        self.transactions_box.configure(state="disabled")

if __name__ == "__main__":
    app = FinanceTrackerApp()
    app.mainloop()
