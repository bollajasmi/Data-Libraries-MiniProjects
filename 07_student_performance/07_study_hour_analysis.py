import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
df = pd.read_csv("07_study_hour_analysis.csv")
# Rank students based on Marks
df["Rank"] = df["Marks"].rank(ascending=False, method="dense")
# Sort by Rank
df = df.sort_values(by="Rank")
# Correlation between Study Hours and Marks
correlation = df["Study_Hours"].corr(df["Marks"])
# Performance Category
df["Performance"] = np.where(df["Marks"] >= 85, "Excellent",
                       np.where(df["Marks"] >= 70, "Good", "Average"))
print("----- Ranked Data -----")
print(df)
print("\nCorrelation between Study Hours and Marks:", correlation)
# 1. Bar chart for Marks by Student
plt.figure()
plt.tight_layout()
plt.subplot(2,2,1)
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks Ranking")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)

# 2. Scatter plot (Study Hours vs Marks)
plt.subplot(2,2,2)
plt.tight_layout()
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
# 3. Pie chart for Performance Categories
performance_counts = df["Performance"].value_counts()
plt.subplot(2,2,3)
plt.tight_layout()
plt.pie(performance_counts.values, labels=performance_counts.index, autopct='%1.1f%%')
plt.title("Performance Distribution")
plt.show()