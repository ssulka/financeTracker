def transaction(date, amount, category, description=None):
    {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    class Transaction:
        def __init__(self, date, amount, category, description=None):
            self.date = date
            self.amount = amount
            self.category = category
            self.description = description

        @classmethod
        def from_dict(cls, data):
            return cls(
                date=data.get("date"),
                amount=data.get("amount"),
                category=data.get("category"),
                description=data.get("description")
            )

        def to_dict(self):
            return {
                "date": self.date,
                "amount": self.amount,
                "category": self.category,
                "description": self.description
            }