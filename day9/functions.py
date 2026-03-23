
def arithmetic(a, b):
    print(f"{a} + {b} = {a + b}")


arithmetic(2, 3)


# create function that takes your age in years, and calculates how many weeks you have to live until 90 years old
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks remaining.")