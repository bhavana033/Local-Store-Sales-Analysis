import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/local_store_sales_cleaned.csv")

# -------------------------
# Basic Business KPIs
# -------------------------
print("========== BUSINESS SUMMARY ==========")

print("Total Revenue :", df["Revenue"].sum())
print("Total Profit :", df["Profit"].sum())
print("Total Orders :", len(df))

print("\nAverage Revenue per Order :",
      round(df["Revenue"].mean(),2))

print("\nHighest Revenue Product:")
print(df.loc[df["Revenue"].idxmax()])

# -------------------------
# Revenue by Category
# -------------------------

category_sales = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Category")
print(category_sales)

# -------------------------
# Revenue by Employee
# -------------------------

employee_sales = df.groupby("Employee")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Employee")
print(employee_sales)

# -------------------------
# Payment Methods
# -------------------------

payment = df["Payment_Method"].value_counts()

print("\nPayment Methods")
print(payment)

plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()