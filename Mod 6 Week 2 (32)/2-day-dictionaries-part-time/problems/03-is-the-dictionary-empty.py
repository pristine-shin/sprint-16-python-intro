# Write a function that returns `True` if a dictionary is empty, and `False`
# otherwise.

# Write your function here.
def is_empty(dictionary):
  return (len(dictionary) == 0)

print(is_empty({}))        #> True
print(is_empty({"a": 1}))  #> False
