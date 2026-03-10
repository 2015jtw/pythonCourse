print("Welcome to the pizza delivery service!")

size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")
bill = 0

#todo: work out how much they need to pay based on their size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":    
    bill += 25
else:
    print("Sorry, we don't have that size of pizza.")

#todo: work out how much to add to their bill based on their pepperoni choice
if add_pepperoni == "Y":
    if size == "S":
        bill += 1
    elif size == "M":
        bill += 2
    else:
        bill += 3

#todo: work out their final amount based on whether they want extra cheese or not
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")