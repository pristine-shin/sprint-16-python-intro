# Create a function that recursively prints a countdown from 5 to 1.

# Write your function here.
def recursive_countdown(num):
    if num <= 1:
        return print(1)
    else:
        print(num)
        return recursive_countdown(num-1)
recursive_countdown(5) #> 5 4 3 2 1
