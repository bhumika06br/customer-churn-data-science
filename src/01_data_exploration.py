import pandas as pd
df=pd.read_csv("data/customer_churn_dataset-testing-master.csv")
print("First 5 rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\ncolumn names: ")
print(df.columns)
print("\nDataset Information: ")
print(df.info())
print("\nMissing Values: ")
print(df.isnull().sum())
print("\nNumerical Statistics: ")
print(df.describe())
print("\nChurn distribution:")
print(df["Churn"].value_counts())  #.value_counts() -> Count how many times each unique value occurs.
print("\nChurn percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

print("\nGender Distribution: ")
print(df["Gender"].value_counts())
print(df["Gender"].value_counts(normalize=True)*100)
print("\n")
print(df["Subscription Type"].value_counts())
print("\n")

import matplotlib.pyplot as plt
# churn_counts=df["Churn"].value_counts()
# plt.bar(["Not churned","Churned"],churn_counts)
# plt.xlabel("Customer status")
# plt.ylabel("Number of customers")
# plt.title("Customer churn distribution")
# plt.show()

print(df.groupby("Churn")["Support Calls"].mean())  #Group customers according to whether they churned, take their Support Calls, and calculate the average for each group.
print(df.groupby("Churn")["Payment Delay"].mean())
print(df.groupby("Churn")["Total Spend"].mean())
print(df.groupby("Subscription Type")["Churn"].mean())

churn_by_subscription=(df.groupby("Subscription Type")["Churn"].mean()*100)
print(churn_by_subscription)
plt.bar(churn_by_subscription.index,churn_by_subscription.values)
plt.xlabel("Subscription Type")
plt.ylabel("Churn Rate(%)")
plt.title("Churn Rate by subscription type")
plt.show()

print(df["Contract Length"].value_counts())

churn_by_contract=df.groupby("Contract Length")["Churn"].mean()*100
print(churn_by_contract)

plt.bar(churn_by_contract.index,churn_by_contract.values)
plt.xlabel("Contract length")
plt.ylabel("Churn rate")
plt.title("Churn rate by contract length")
plt.show()