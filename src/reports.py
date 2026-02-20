from datetime import datetime
import os

def generate_report(expenses, report_name):
    """
    Generates a text report summarizing expenses and saves it to a file.
    :param expenses: The list of Expense objects.
    :param report_name: The base name for the report file.
    """
    if not expenses:
        print("No expenses recorded to generate a report.")
        return

    # 1. Total Expenses
    total_expenses = sum(e.amount for e in expenses)

    # 2. Category-wise Summary
    category_summary = {}
    for expense in expenses:
        category = expense.category
        category_summary[category] = category_summary.get(category, 0.0) + expense.amount

    # 3. Monthly Summary (for the current data set)
    # Get the month and year of the earliest and latest entry
    dates = [datetime.strptime(e.date, "%Y-%m-%d") for e in expenses]
    start_date = min(dates).strftime("%Y-%m-%d")
    end_date = max(dates).strftime("%Y-%m-%d")

    # 4. Generate Report Content
    report_content = f"""
==================================================
           FINANCE REPORT: {report_name.upper()}
==================================================
Analysis Period: {start_date} to {end_date}

TOTAL EXPENSES: ₹{total_expenses:,.2f}
--------------------------------------------------
CATEGORY-WISE BREAKDOWN:

{'Category':<20} | {'Total Amount (₹)':<20} | {'Percentage (%)':<10}
{'-'*60}
"""

    # Add category details
    sorted_categories = sorted(category_summary.items(), key=lambda item: item[1], reverse=True)
    for category, total in sorted_categories:
        percentage = (total / total_expenses) * 100 if total_expenses else 0
        report_content += f"{category:<20} | {total:20,.2f} | {percentage:10.2f}\n"

    report_content += "\n--------------------------------------------------"
    report_content += f"\nNote: All figures are in Indian Rupees (₹)."
    report_content += f"\nReport Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    # 5. Save Report to File
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{report_name.lower().replace(' ', '_')}_{timestamp}.txt"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"\n✅ Report saved successfully to {filename}")
        print("-" * 50)
        print(report_content)
        print("-" * 50)
    except IOError as e:
        print(f"❌ ERROR: Could not save report file. {e}")

    return total_expenses, category_summary