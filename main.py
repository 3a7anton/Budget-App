class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line
        title = f"{self.name:*^30}"
        # List of items in the ledger
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
        # Category total
        total = f"Total: {self.get_balance():.2f}"
        # Full budget category report
        return f"{title}\n{items}{total}"

def create_spend_chart(categories):
    # Calculate percentage spent in each category
    total_withdrawals = sum(category.get_balance() for category in categories)
    percentages = [int(category.get_balance() / total_withdrawals * 10) * 10 for category in categories]
    # Build chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    # Add category names at the bottom
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += " " * 5
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"
    return chart
