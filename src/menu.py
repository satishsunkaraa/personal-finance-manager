from src.file_manager import load_expenses, save_expenses, backup_data
from src.expense import Expense
from src.utils import get_valid_amount, get_valid_category, get_valid_date, VALID_CATEGORIES
from src.reports import generate_report

EXPENSES = load_expenses()

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*45)
    print(" " * 8 + "PERSONAL FINANCE MANAGER (STANDARD)")
    print("="*45)
    print("MAIN MENU:")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Category-wise Summary")
    print("4. Generate Comprehensive Report")
    print("5. Search Expenses by Category/Description")
    print("6. Backup Data")
    print("7. Exit & Save")
    print("-" * 45)

def add_expense():
    """Handles the process of adding a new expense."""
    print("\n--- ADD NEW EXPENSE ---")
    
    # Get validated user input using utility functions
    amount = get_valid_amount("Enter amount: ")
    category = get_valid_category(f"Enter category")
    date = get_valid_date("Enter date")
    description = input("Enter description: ").strip()

    # Create and add the expense
    new_expense = Expense(amount, category, date, description)
    EXPENSES.append(new_expense)
    print("\n✅ Expense added successfully!")

def view_expenses():
    """Displays all recorded expenses."""
    print("\n--- ALL RECORDED EXPENSES ---")
    if not EXPENSES:
        print("No expenses recorded yet.")
        return
    
    for i, expense in enumerate(EXPENSES, 1):
        print(f"{i:3}. {expense}")

def view_category_summary():
    """Calculates and displays the category-wise total expenses."""
    print("\n--- CATEGORY-WISE SUMMARY ---")
    if not EXPENSES:
        print("No expenses recorded yet.")
        return

    summary = {}
    total = 0.0
    for expense in EXPENSES:
        summary[expense.category] = summary.get(expense.category, 0.0) + expense.amount
        total += expense.amount

    print(f"Total Expenses: ₹{total:,.2f}\n")
    print(f"{'Category':<20} | {'Total Amount (₹)':<20} | {'Percentage (%)':<10}")
    print("-" * 55)

    sorted_summary = sorted(summary.items(), key=lambda item: item[1], reverse=True)
    for category, amount in sorted_summary:
        percentage = (amount / total) * 100 if total else 0
        print(f"{category:<20} | {amount:20,.2f} | {percentage:10.2f}")

def search_expenses():
    """Allows searching expenses by category or description keyword."""
    print("\n--- SEARCH EXPENSES ---")
    search_term = input("Enter category or description keyword to search: ").strip().lower()
    
    if not search_term:
        print("Search term cannot be empty.")
        return

    results = [
        e for e in EXPENSES 
        if search_term in e.category.lower() or search_term in e.description.lower()
    ]

    if not results:
        print(f"No expenses found matching '{search_term}'.")
        return

    print(f"\nFound {len(results)} expenses matching '{search_term}':")
    print("-" * 45)
    for expense in results:
        print(expense)
    print("-" * 45)

def run_menu():
    """The main loop for the application menu."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                view_category_summary()
            elif choice == '4':
                generate_report(EXPENSES, "Comprehensive Report")
            elif choice == '5':
                search_expenses()
            elif choice == '6':
                backup_data()
            elif choice == '7':
                print("\nSaving data and exiting...")
                save_expenses(EXPENSES)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except Exception as e:
            # Catch-all for unexpected errors
            print(f"\n❌ An unexpected error occurred: {e}")
            print("Please try again.")
        finally:
            if choice != '7':
                input("\nPress Enter to return to the menu...")

# Note: The data is initially loaded when the module is imported (EXPENSES = load_expenses())