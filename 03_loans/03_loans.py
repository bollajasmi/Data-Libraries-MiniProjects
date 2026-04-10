import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
loan = pd.read_csv("03_loan.csv")

print("Full Data:\n", loan)
# Eligibility
loan["Eligible"] = np.where(
    (loan["Income"] > 35000) & (loan["Credit_Score"] > 700),
    "Yes", "No"
)
# Eligible clients
eligible_clients = loan[loan["Eligible"] == "Yes"]
# Average income
avg_income = loan["Income"].mean()
# Highest income client
highest_income = loan.loc[loan["Income"].idxmax()]
# Lowest credit score
lowest_credit = loan.loc[loan["Credit_Score"].idxmin()]
# Eligibility count
eligibility_count = loan["Eligible"].value_counts()
# Avg credit score by eligibility
avg_credit_by_group = loan.groupby("Eligible")["Credit_Score"].mean()
# Correlation
correlation = loan["Income"].corr(loan["Credit_Score"])
print("\nEligible Clients:\n", eligible_clients)
print("\nAverage Income:", avg_income)
print("\nHighest Income:\n", highest_income)
print("\nLowest Credit Score:\n", lowest_credit)
print("\nEligibility Count:\n", eligibility_count)
print("\nAvg Credit Score by Group:\n", avg_credit_by_group)
print("\nCorrelation (Income vs Credit Score):", correlation)

plt.figure()
# 1. Bar chart (Eligibility count)
plt.subplot(2, 2, 1)
plt.bar(eligibility_count.index, eligibility_count.values)
plt.title("Eligibility Count")

# 2. Line chart (Income trend)
plt.subplot(2, 2, 2)
plt.plot(loan.index, loan["Income"])
plt.title("Income Trend")
plt.xlabel("Client Index")
plt.ylabel("Income")

# 3. Pie chart (Eligibility distribution)
plt.subplot(2, 2, 3)
plt.pie(eligibility_count.values, labels=eligibility_count.index, autopct='%1.1f%%')
plt.title("Eligibility Distribution")

# 4. Scatter plot (Income vs Credit Score)
plt.subplot(2, 2, 4)
plt.scatter(loan["Income"], loan["Credit_Score"])
plt.title("Income vs Credit Score")
plt.xlabel("Income")
plt.ylabel("Credit Score")

plt.tight_layout()
plt.show()