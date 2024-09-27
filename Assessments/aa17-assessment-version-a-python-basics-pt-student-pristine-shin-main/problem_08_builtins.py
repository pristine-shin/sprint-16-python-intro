# BUILTINS
#
# Write a function named "square_lists" that accepts an iterable containing lists
# and returns a new list where each inner list's elements are squared.

# Use the "map" method along with a lambda function to do this.

# Test data is at the bottom.

# WRITE YOUR CODE HERE
# Your code here
def square_lists(nestedLst):
  return list(map(lambda innerLst: [n**2 for n in innerLst], nestedLst))

# TEST DATA
print(square_lists([[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]))
# Prints [[1], [1, 4], [1, 4, 9], [1, 4, 9, 16]]

print(square_lists([]))  # Prints []
