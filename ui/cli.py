import argparse

def add_transaction(amount, category, description):
    # Logic to add a transaction
    print(f"Added transaction: {amount} {category} {description}")

def view_transactions():
    # Logic to view transactions
    print("Viewing all transactions...")

def main():
    parser = argparse.ArgumentParser(description="Finance Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add transaction command
    add_parser = subparsers.add_parser("add", help="Add a new transaction")
    add_parser.add_argument("amount", type=float, help="Transaction amount")
    add_parser.add_argument("category", type=str, help="Transaction category")
    add_parser.add_argument("description", type=str, help="Transaction description")

    # View transactions command
    view_parser = subparsers.add_parser("view", help="View all transactions")

    args = parser.parse_args()

    if args.command == "add":
        add_transaction(args.amount, args.category, args.description)
    elif args.command == "view":
        view_transactions()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()