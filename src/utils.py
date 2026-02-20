from datetime import datetime

VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Salary", "Other"]

def is_valid_date(date_str, date_format="%Y-%m-%d"):
    """
    Validates if a string is a valid date in the specified format.
    :param date_str: The string to validate.
    :param date_format: The expected date format.
    :return: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

def get_valid_amount(prompt):
    """
    Prompts the user for a numerical amount and handles errors.
    """
    while True:
        try:
            amount = input(prompt).strip()
            # Check for empty input
            if not amount:
                print("Amount cannot be empty.")
                continue
            
            # Convert and check if non-negative
            value = float(amount)
            if value < 0:
                print("Amount must be a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")

def get_valid_category(prompt):
    """
    Prompts the user for a category and ensures it is one of the valid options.
    """
    category_list = "/".join(VALID_CATEGORIES)
    while True:
        category = input(f"{prompt} ({category_list}): ").strip().title()
        if category in VALID_CATEGORIES:
            return category
        else:
            print(f"Invalid category. Must be one of: {category_list}")

def get_valid_date(prompt):
    """
    Prompts the user for a date and ensures it is in the YYYY-MM-DD format.
    """
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD): ").strip()
        if is_valid_date(date_str):
            return date_str
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")