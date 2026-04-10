import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv("08_sales_analysis.csv")

print("Full Data:\n", sales)
# Revenue column
sales["Revenue"] = sales["Quantity"] * sales["Price"]
# Convert Date
sales["Date"] = pd.to_datetime(sales["Date"])
# Daily revenue
daily_revenue = sales.groupby("Date")["Revenue"].sum()
# Top product
top_product = sales.groupby("Product")["Quantity"].sum().idxmax()
# Total revenue
total_revenue = sales["Revenue"].sum()
# Average revenue
avg_revenue = sales["Revenue"].mean()
# Highest revenue day
best_day = daily_revenue.idxmax()
# Product-wise revenue
product_revenue = sales.groupby("Product")["Revenue"].sum()
# Above average sales
above_avg = sales[sales["Revenue"] > avg_revenue]
# Correlation
correlation = sales["Quantity"].corr(sales["Price"])
print("\nDaily Revenue:\n", daily_revenue)
print("\nTop Product:", top_product)
print("\nTotal Revenue:", total_revenue)
print("\nAverage Revenue:", avg_revenue)
print("\nBest Day:", best_day)
print("\nProduct Revenue:\n", product_revenue)
print("\nAbove Average Sales:\n", above_avg)
print("\nCorrelation (Quantity vs Price):", correlation)

plt.figure()
# 1. Line chart (Daily revenue trend)
plt.subplot(2, 2, 1)
plt.plot(daily_revenue.index, daily_revenue.values)
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
# 2. Bar chart (Revenue per product)
plt.subplot(2, 2, 2)
plt.bar(product_revenue.index, product_revenue.values)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
# 3. Pie chart (Product share)
plt.subplot(2, 2, 3)
plt.pie(product_revenue.values, labels=product_revenue.index, autopct='%1.1f%%')
plt.title("Product Revenue Share")
# 4. Scatter plot (Quantity vs Price)
plt.subplot(2, 2, 4)
plt.scatter(sales["Quantity"], sales["Price"])
plt.title("Quantity vs Price")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.tight_layout()
plt.show()