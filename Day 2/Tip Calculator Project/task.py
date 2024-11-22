print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? PHP"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% "))
people = int(input("How many people to split the bill? "))

#math operators
tip_percentage = float(tip / float(100))
tip_value = float(bill * tip_percentage)
total_bill_tip = float(bill + tip_value)
result = float(total_bill_tip / float(people))

print(f"Each person should pay: PHP{round(result, 2)}")


