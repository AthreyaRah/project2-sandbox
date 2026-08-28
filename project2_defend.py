def main():
    # summarize_expenses(100, 250, 75, category="food", month="August")
    summarize_expenses()

    expenses = [
        {"item": "coffee", "amount": 150},
        {"item": "rent", "amount": 20000},
        {"item": "snacks", "amount": 80},
    ]
    print([expense["item"] for expense in expenses if expense["amount"] > 100])
    print({expense["item"]:expense["amount"] for expense in expenses})

    meal = Expense("lunch", 300)
    daily_meal = RecurringExpense("Lunch", 300, "daily")
    print(meal.describe())
    print(daily_meal.describe())

    print(safe_divide_expense(125,2))
    try:
        print(safe_divide_expense(125,0))
    except ZeroDivisionError as e:
        print(e)
    try:
        print(safe_divide_expense(125,"10"))
    except TypeError as e:
        print(e)


class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount


    def describe(self):
        return f"{self.item}: {self.amount}"


class RecurringExpense(Expense):
    def __init__(self,item,amount, frequency):
        super().__init__(item,amount)
        self.frequency = frequency

    def describe(self):
        item_amount = super().describe()
        return f"{item_amount} ({self.frequency})"



def summarize_expenses(*amounts, **labels):
    print(f"Total: {sum(amounts)}")
    for key,value in labels.items():
        print(f"{key}: {value}")


def safe_divide_expense(total,count):
    try:
        quotient = total/count
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"denominator cannot be 0") from e
    except TypeError as e:
        raise TypeError(f"Invalid type for denominator, {count} should be a number") from e
    return quotient




if __name__ == "__main__":
    main()