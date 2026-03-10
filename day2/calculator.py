# ask the total bill
bill = float(input("What was the total bill? $"))

# ask the tip > 10, 12, or 15
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# ask how many people to split the bill
people = int(input("How many people to split the bill? "))

# determine how much each person should pay (round to 2 decimal places)
total = bill + (bill * tip / 100)
each = round(total / people, 2)

print(f"Each person should pay: ${each}")