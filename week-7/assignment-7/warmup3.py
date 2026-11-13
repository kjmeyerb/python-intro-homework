import os
print("--------------------------")
print(f"Current Working Directory: \n {os.getcwd()}")
print("--------------------------")
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
print("--------------------------")
path = os.path.join("..", "data", "expenses.csv")
print(f"Path from cwd: {path}")