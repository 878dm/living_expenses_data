# Calculate the total expenses
import json
f=open("data.json")
x=f.read()
monthly_expenses=json.loads(x)
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    total=0
    for i in monthly_expenses.values():
        total+=i
    return total


print(total_expenses(monthly_expenses))