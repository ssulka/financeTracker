import matplotlib.pyplot as plt

def plot_expenses(categories, amounts):
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    categories = ['Food', 'Rent', 'Utilities', 'Entertainment']
    amounts = [250, 1200, 300, 150]
    plot_expenses(categories, amounts)