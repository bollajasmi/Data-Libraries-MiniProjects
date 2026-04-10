import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data
bus = pd.read_csv("10_transport.csv")
print("Full Data:\n", bus)

# Total transport fee
total_transport = bus["Monthly_Fee"].sum()
# Average fee per route
avg_fee_per_route = bus.groupby("Route")["Monthly_Fee"].mean()
# Highest paying student
highest_fee = bus.loc[bus["Monthly_Fee"].idxmax()]
# Lowest paying student
lowest_fee = bus.loc[bus["Monthly_Fee"].idxmin()]
# Total students per route
students_per_route = bus["Route"].value_counts()
# Fee category
bus["Fee_Category"] = np.where(bus["Monthly_Fee"] > 1500, "High",
                         np.where(bus["Monthly_Fee"] > 800, "Medium", "Low"))
# Average fee
avg_fee = np.mean(bus["Monthly_Fee"])
# Above average fee students
above_avg = bus[bus["Monthly_Fee"] > avg_fee]

print("\nTotal Transport Fee:", total_transport)
print("\nAverage Fee per Route:\n", avg_fee_per_route)
print("\nHighest Fee Details:\n", highest_fee)
print("\nLowest Fee Details:\n", lowest_fee)
print("\nStudents per Route:\n", students_per_route)
print("\nAverage Fee:", avg_fee)
print("\nAbove Average Fee Students:\n", above_avg)

plt.figure()
# 1. Bar chart (Average fee per route)
plt.subplot(2, 2, 1)
plt.bar(avg_fee_per_route.index, avg_fee_per_route.values)
plt.title("Avg Fee per Route")
plt.xlabel("Route")
plt.ylabel("Fee")
# 2. Line chart (Fee trend)
plt.subplot(2, 2, 2)
plt.plot(bus.index, bus["Monthly_Fee"])
plt.title("Fee Trend")
plt.xlabel("Index")
plt.ylabel("Fee")
# 3. Pie chart (Fee category distribution)
plt.subplot(2, 2, 3)
category_counts = bus["Fee_Category"].value_counts()
plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
plt.title("Fee Category Distribution")
# 4. Bar chart (Students per route)
plt.subplot(2, 2, 4)
plt.bar(students_per_route.index, students_per_route.values)
plt.title("Students per Route")
plt.xlabel("Route")
plt.ylabel("Count")
plt.tight_layout()
plt.show()