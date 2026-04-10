import numpy as np
import pandas as pd

df=pd.read_csv("orders.csv")
print(df)

#total revenue non returning
total_revenue=df[df["Returned"] =="No"]["Price"].sum()
print("total revenue:",total_revenue)
#return loss
return_loss=df[df["Returned"]=="Yes"]["Price"].sum()
print("return_loss:",return_loss)
#return rate
return_rate=df[df["Returned"]=="Yes"]["Price"].mean() *100
print("return_rate:",return_rate)
#most returned product
most_returned_pdt=df[df["Returned"]=="Yes"].groupby("Product").size().idxmax()
print("most returned product:",most_returned_pdt)

