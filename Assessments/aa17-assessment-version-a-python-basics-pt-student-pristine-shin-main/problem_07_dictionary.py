# DICTIONARY
#
# Write a function named "my_filter" that takes a dictionary as a parameter.
# Return another dictionary that consists of the key/value pairs from the
# argument where the value has a length less than or equal to 3. Use any
# construct you would like to implement "my_filter".
#
# Test data follows.

# WRITE YOUR CODE HERE
# Your code here
def my_filter(dictionary):
  return {k:v for k, v in dictionary.items() if len(v) <= 3}

# TEST DATA
print(my_filter({1: ".", 2: "..", 5: "....."}))   # > {1: ".", 2: ".."}
print(my_filter({}))                              # > {}
print(my_filter({1: ".....", 2: "....", 5: ""}))  # > {5: ""}
