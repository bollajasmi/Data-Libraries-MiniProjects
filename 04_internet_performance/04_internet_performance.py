import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

internet = pd.read_csv("04_internet_performance.csv")
print("Full Data:\n", internet)
# Connection Quality
internet["Connection_Quality"] = np.where(
    internet["Ping"] < 30, "Excellent",
    np.where(internet["Ping"] <= 50, "Good", "Poor")
)
# Fastest user
fastest_user = internet.loc[internet["Download_Speed"].idxmax()]
# Slowest user
slowest_user = internet.loc[internet["Download_Speed"].idxmin()]

# Average speeds
avg_download = internet["Download_Speed"].mean()
avg_upload = internet["Upload_Speed"].mean()
# Quality count
quality_count = internet["Connection_Quality"].value_counts()
# Avg speed by quality
avg_speed_by_quality = internet.groupby("Connection_Quality")["Download_Speed"].mean()
# Correlation
correlation = internet["Ping"].corr(internet["Download_Speed"])

print("\nFastest User:\n", fastest_user)
print("\nSlowest User:\n", slowest_user)
print("\nAverage Download Speed:", avg_download)
print("\nAverage Upload Speed:", avg_upload)
print("\nConnection Quality Count:\n", quality_count)
print("\nAvg Speed by Quality:\n", avg_speed_by_quality)
print("\nCorrelation (Ping vs Download Speed):", correlation)
plt.figure()
# 1. Bar chart (Download speed per user)
plt.subplot(2, 2, 1)
plt.bar(internet.index.astype(str), internet["Download_Speed"])
plt.title("Download Speed per User")
plt.xlabel("User Index")
plt.ylabel("Speed")
# 2. Line chart (Ping trend)
plt.subplot(2, 2, 2)
plt.plot(internet.index, internet["Ping"])
plt.title("Ping Trend")
plt.xlabel("User Index")
plt.ylabel("Ping")
# 3. Pie chart (Connection Quality)
plt.subplot(2, 2, 3)
plt.pie(quality_count.values, labels=quality_count.index, autopct='%1.1f%%')
plt.title("Connection Quality Distribution")
# 4. Scatter plot (Ping vs Download Speed)
plt.subplot(2, 2, 4)
plt.scatter(internet["Ping"], internet["Download_Speed"])
plt.title("Ping vs Download Speed")
plt.xlabel("Ping")
plt.ylabel("Download Speed")

plt.tight_layout()
plt.show()