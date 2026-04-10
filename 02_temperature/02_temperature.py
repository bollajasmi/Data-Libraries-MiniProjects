import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

data = pd.read_csv("01_temperature.csv")

print("temperature data:\n")
print(data)

# convert date column into datetime
data["Date"] = pd.to_datetime(data["Date"])

# avg temp
temp_avg = np.mean(data["Temperature"])
print("\naverage temperature:")
print(temp_avg)

# hottest day
hottest = data.loc[data["Temperature"].idxmax()]
print("\nhottest day:")
print(hottest)

# coldest day
coldest = data.loc[data["Temperature"].idxmin()]
print("\ncoldest day:")
print(coldest)

# above average
above_average = data[data["Temperature"] > temp_avg]
print("\nabove average days:")
print(above_average)

print("\nno.of days above average:", len(above_average))


# 1. Line graph
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(data["Date"], data["Temperature"])
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()

# 2. Bar chart
plt.subplot(2, 2, 2)
plt.bar(data["Date"].astype(str), data["Temperature"])
plt.title("Daily Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
# 3. Pie Chart (Above vs Below Average Days)
plt.subplot(2, 2, 3)
labels = ["Above Avg", "Below Avg"]
sizes = [len(above_average), len(data) - len(above_average)]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Above vs Below Average Temperature Days")
plt.tight_layout()

# 4. Histogram (Temperature Distribution)
plt.subplot(2, 2, 4)
plt.hist(data["Temperature"])
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
