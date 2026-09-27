import numpy as np
monthly_charges=np.array([70,45,80,55,100,50,90,67,84,79])
print("Monthly charges: ",monthly_charges)
average_charge=np.mean(monthly_charges)
print("Average monthly charge: ",average_charge)
highest_charge=np.max(monthly_charges)
print("Highest charge: ",highest_charge)
lowest_charge = np.min(monthly_charges)
print("Lowest monthly charge:", lowest_charge)
total_charges = np.sum(monthly_charges)
print("Total:", total_charges)

# count=0
# for i in range(len(monthly_charges)):
#     if monthly_charges[i]>75:
#         count+=1
# print(count)

# numpy way of doing this
count=np.sum(monthly_charges<=50)
print(count)


