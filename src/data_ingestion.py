import pandas as pd
import os
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv")
print(df.iloc[0])

df = df.drop(columns=["Email", "Address", "Avatar", "Avg. Session Length"])
df = df[df["Length of Membership"] > 1]
print(df.shape)

df.to_csv(os.path.join("data", "cleaned_data.csv"), index=False)