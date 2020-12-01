# import random module
import random

# use input to collect starting value , ending value
a, b = input('enter starting value and ending value').split()

# we use randint() for get random integer number
print(random.randint(int(a), int(b)))