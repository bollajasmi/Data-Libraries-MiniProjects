import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

df = pd.read_csv("05_vehicle_efficiency.csv")

# Create Mileage column
df["Mileage"] = df["Distance_Travelled"] / df["Petrol_Used"]

avg_milage = df["Mileage"].mean()

# best mileage day
best_day = df.loc[df["Mileage"].idxmax()]

# standard deviation
std_milage = np.std(df["Mileage"])

# totals
petrol_used = df["Petrol_Used"].sum()
distance_travelled = df["Distance_Travelled"].sum()

print(df)
print("\navg_milage:", avg_milage)
print("\nbest_day:\n", best_day)
print("\nstd.milage:", std_milage)
print("\npetrol_used:", petrol_used)
print("\ndistance_travelled:", distance_travelled)

plt.figure()

# 1. Line Chart (Mileage trend)
plt.subplot(2, 2, 1)
plt.plot(df.index, df["Mileage"])
plt.title("Mileage Trend")
plt.xlabel("Day Index")
plt.ylabel("Mileage")

# 2. Bar Graph (Distance per Day)
plt.subplot(2, 2, 2)
plt.bar(df.index.astype(str), df["Distance_Travelled"])
plt.title("Distance Travelled")
plt.xlabel("Day")
plt.ylabel("Distance")

# 3. Pie Chart (Petrol vs Distance contribution)
plt.subplot(2, 2, 3)
plt.pie([petrol_used, distance_travelled],
        labels=["Petrol Used", "Distance Travelled"],
        autopct='%1.1f%%')
plt.title("Petrol vs Distance")

# 4. Scatter Plot (Petrol vs Distance)
plt.subplot(2, 2, 4)
plt.scatter(df["Petrol_Used"], df["Distance_Travelled"])
plt.title("Petrol vs Distance Relation")
plt.xlabel("Petrol Used")
plt.ylabel("Distance Travelled")

plt.tight_layout()
plt.show()
