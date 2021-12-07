from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []

# Fügt die Kategorien der neu erzeugten Liste hinzu
for expense in expenses.list:
  spending_categories.append(expense.category)

# Ordnet die Elemente nach Häufigkeit in der Übergebenen Liste als key:value bzw. category:count
spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title("# of Purchases by Category")
plt.show()