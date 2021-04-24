# Randomize list elements

from random import *

n = list(range(10))
n2 = n

print(f"Default list: {n}")

for i in range(len(n)):
    index = randrange(10)
    n[i], n[index] = n[index], n[i]
print(f"Shuffled list: {n}")

shuffle(n2)
print(f"Shuffled list: {n2}")
