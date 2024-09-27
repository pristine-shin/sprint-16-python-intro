# WHILE LOOP
#
# In this problem, write a function named "my_while_map" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are all transformed to upper case. The function must
# use a while loop in its implementation.
#
# The str object in Python has a method on it named "upper".
#
# There are two sample data calls for you to use.

# WRITE YOUR FUNCTION HERE

# Your code here
def my_while_map(lst):
  idx = 0
  result = []
  while idx < len(lst):
    result.append(lst[idx].upper())
    idx += 1
  return result

# TEST DATA

test = ["plop", "", "drop", "zop", "stop"]
print(my_while_map(test))  # > ["PLOP", "", "DROP", "ZOP", "STOP"]

test = []
print(my_while_map(test))  # > []
