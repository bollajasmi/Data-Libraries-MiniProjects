import pandas as pd
import numpy as np

df = pd.read_csv("performance.csv")

# Rank students based on Marks
df["Rank"] = df["Marks"].rank(ascending=False,method="dense")

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