import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
# Read file
df = pd.read_csv("09_sleep.csv")
# Average sleep
avg_sleep = df["Sleep_Hours"].mean()
# Maximum productivity
max_productivity = df["Productivity"].max()
# Days with less than 6 hours sleep
less_sleep = df[df["Sleep_Hours"] < 6]
print("Full Data:\n", df)
print("\nAverage Sleep:", avg_sleep)
print("Maximum Productivity:", max_productivity)
print("\nDays with less sleep:\n", less_sleep)
# Sleep Quality
df["Sleep_Quality"] = np.where(
    df["Sleep_Hours"] > 7, "Good",
    np.where(df["Sleep_Hours"] < 4, "Poor", "Average")
)
# Correlation
correlation = df["Sleep_Hours"].corr(df["Productivity"])
print("----- Full Data -----")
print(df)
print("\nCorrelation:", correlation)
# 1. Bar chart (Sleep Hours per Day)
plt.figure()
plt.subplot(2, 2, 1)
plt.bar(df.index.astype(str), df["Sleep_Hours"])
plt.title("Sleep Hours per Day")
plt.xlabel("Day Index")
plt.ylabel("Sleep Hours")
# 2. Scatter plot (Sleep vs Productivity)
plt.subplot(2, 2, 2)
plt.scatter(df["Sleep_Hours"], df["Productivity"])
plt.title("Sleep Hours vs Productivity")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity")
# 3. Pie chart (Sleep Quality Distribution)
quality_counts = df["Sleep_Quality"].value_counts()
plt.subplot(2, 2, 3)
plt.pie(quality_counts.values, labels=quality_counts.index, autopct='%1.1f%%')
plt.title("Sleep Quality Distribution")
# 4. Line graph (Trend)
plt.subplot(2, 2, 4)
plt.plot(df.index, df["Sleep_Hours"], label="Sleep Hours")
plt.plot(df.index, df["Productivity"], label="Productivity")
plt.title("Sleep vs Productivity Trend")
plt.xlabel("Day Index")
plt.ylabel("Values")
plt.legend()
plt.show()




