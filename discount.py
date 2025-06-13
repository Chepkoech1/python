# Write a program to assign a discount of 5% if amount of purchase exceeds KSh 1,000


amount = int(input("Enter amount : "))

if amount > 1000:
    amount = amount * 0.05 



print("Amount to pay: KSh " + str(round(amount, 2)))

