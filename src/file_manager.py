import csv
import os
from datetime import datetime
from src.expense import Expense

FILE_PATH = 'data/expenses.csv'
HEADER = ['Date', 'Category', 'Amount', 'Description']

def _ensure_file_exists():
    """
    Checks if the data file exists and creates it with headers if not.
    """
    if not os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(HEADER)
        except IOError as e:
            print(f"ERROR: Could not create data file. {e}")

def load_expenses():
    """
    Loads all expenses from the CSV file.
    :return: A list of Expense objects.
    """
    _ensure_file_exists()
    expenses = []
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            # --- START FIX FOR StopIteration ERROR ---
            try:
                next(reader)  # Skip header row
            except StopIteration:
                # If the file is newly created or only contains the header row, 
                # next() will raise StopIteration. We catch it and return an empty list.
                return expenses 
            # --- END FIX ---
            
            for row in reader:
                try:
                    # Basic validation (4 columns expected)
                    if len(row) == 4:
                        expenses.append(Expense.from_csv_row(row))
                except (ValueError, IndexError) as e:
                    print(f"Warning: Skipping malformed row in CSV: {row}. Error: {e}")
    except IOError:
        print("INFO: Data file not found or could not be read. Starting with an empty list.")
    return expenses

def save_expenses(expenses):
    """
    Writes the list of Expense objects back to the CSV file.
    :param expenses: A list of Expense objects.
    """
    try:
        with open(FILE_PATH, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
            for expense in expenses:
                writer.writerow(expense.to_list())
        # print("Data saved successfully.")
    except IOError as e:
        print(f"ERROR: Could not save data to file. {e}")

def backup_data():
    """
    Creates a timestamped backup of the current expenses.csv file.
    """
    if not os.path.exists(FILE_PATH):
        print("No data file to backup.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"data/expenses_backup_{timestamp}.csv"
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as src, \
             open(backup_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())
        print(f"✅ Data successfully backed up to {backup_file}")
    except IOError as e:
        print(f"❌ Backup failed: {e}")