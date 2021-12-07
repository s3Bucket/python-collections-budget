from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []

# Fügt die Kategorien der neu erzeugten Liste hinzu
for expense in expenses.list:
  spending_categories.append(expense.category)

# Ordnet die Elemente nach Häufigkeit in der Übergebenen Liste als key:value bzw. category:count
spending_counter = collections.Counter(spending_categories)

print(spending_categories)
print(spending_counter)