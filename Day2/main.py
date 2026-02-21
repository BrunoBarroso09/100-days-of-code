#Day 2 Project: Tip calculator

print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $ "))
tip = float(input("How much tip would like to give? 10, 12 or 15? "))
people_split = float(input("How many people to split the bill?"))
total_pay = ((total_bill * (tip / 100)) + total_bill) / people_split

print(f"Each person pay: $ {total_pay:.2f}")