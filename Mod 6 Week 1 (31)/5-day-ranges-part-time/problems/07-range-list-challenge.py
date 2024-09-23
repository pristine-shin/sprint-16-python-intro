# Create a function that returns a list of 100 randomly generated numbers.

import random

# Write your function here.
def rng(list):
  for i in range(100):
    list.append(random.randrange(101))
  return list

print(rng([]))
