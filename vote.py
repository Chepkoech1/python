# write a program to check if a person is eligible to vote. THe person must be a kenyan citizen and above 18 years


# age = int(input("Enter your age: "))
# citizen = (input("Are you a Kenyan citizen? (yes/no): "))

# if (age > 18 and citizen == "yes"):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")



    # must be east african citizen
age = int(input("Enter your age: "))
citizen = (input("Enter your your country name? : ")).upper()
           

if (age >= 18 and citizen in ["Kenya","Uganda","Tanzania"]):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")