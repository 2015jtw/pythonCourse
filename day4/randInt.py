import random
import my_module

number = random.randint(1, 100)
print(number)

print(my_module.my_fav_num)

randFloat = random.random() * 100

print(randFloat) 

heads_or_tails = random.randint(0, 1)
print(heads_or_tails)

if heads_or_tails == 1:
    print("Heads")
else:    
    print("Tails")