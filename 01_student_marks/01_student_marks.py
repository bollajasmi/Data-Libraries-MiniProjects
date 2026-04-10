import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
data = pd.read_csv("01_student_marks.csv")
print("student data:\n")
print(data)
# average marks
data["average"] = data[["eng", "math", "sci"]].mean(axis=1)
print("\naverage marks of students\n")
print(data[["name", "average"]])
# subject wise avg
sub_average = data[["eng", "math", "sci"]].mean()
print("\nsubject wise average\n:")
print(sub_average)
# topper & lowest
highest = data.loc[data["average"].idxmax()]
lowest = data.loc[data["average"].idxmin()]
print("\ntopper details\n:")
print(highest)
print("\nlowest scorer:\n")
print(lowest)
# class average
class_avg = np.mean(data["average"])
print("\nclass average:\n")
print(class_avg)
# 1. Bar graph for student averages
plt.figure()
plt.subplot(2, 2, 1)
plt.bar(data["name"], data["average"])
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
# 2. Subject-wise average bar chart
plt.subplot(2, 2, 2)
plt.bar(sub_average.index, sub_average.values)
plt.title("Subject-wise Average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
# 3. Pie chart 
plt.subplot(2, 2, 3)
plt.pie(sub_average.values, labels=sub_average.index, autopct='%1.1f%%')
plt.title("Subject Contribution")
plt.tight_layout()
plt.show()
