print("Welcome to Tip Calcultor!")
bill=float(input("What was total bill? $"))
tip=int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
total=bill*(1+tip/100)
splitted_pay=total/people
splitted_pay=round(splitted_pay,2)
print(f"Each person should pay: ${splitted_pay}")