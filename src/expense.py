class Expense:
    """
    Represents a single financial expense.
    """
    def __init__(self, amount, category, date, description):
        """
        Initializes an Expense object.
        :param amount: The expense amount (float).
        :param category: The expense category (string).
        :param date: The expense date (YYYY-MM-DD string).
        :param description: A brief description (string).
        """
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        """
        Returns a user-friendly string representation of the expense.
        """
        return f"{self.date} | {self.category.ljust(15)}: ₹{self.amount:,.2f} - {self.description}"

    def to_list(self):
        """
        Converts the expense object into a list for CSV writing.
        """
        return [self.date, self.category, self.amount, self.description]

    @classmethod
    def from_csv_row(cls, row):
        """
        Creates an Expense object from a list (row from CSV).
        :param row: A list of [date, category, amount, description].
        :return: An Expense object.
        """
        # Note: CSV row is [Date, Category, Amount, Description]
        return cls(amount=row[2], category=row[1], date=row[0], description=row[3])