# In Python, error handling can be done using a `try`/`except` block. Implement
# `except` blocks to handle the exceptions that will be raised for the following
# `try` blocks:

# Example 1
try:
    str = 'hello'
    str[0] = 'm'
    print(str)
except TypeError as e:
    print(e, "Strings are immutable")
finally:
    print('I happen regardless of any exceptions.')

# Example 2
try:
    print(x)
except NameError:
    print("you just got a name error")
finally:
    print('I happen regardless of any exceptions.')
