# It's time to explore the *tuple* object and how to use it.

# Follow the instructions in the code comments. Be sure to test your work by
# running your code!

# For the bonus, remember you can split a returned tuple to variables: `(a,b,c)
# = myfunc()`

# DO NOT EDIT
odds = 1,3,5,7,9
evens = 2,4,6,8

# Step 1: Print out the result of adding evens to odds
print(tuple([e + o for e in evens for o in odds]))

# Step 2: Print out the result of multiplying odds by three
print(tuple([3 * o for o in odds]))

# Step 3A: Use print to find out if odds is less than evens
print([o < e for e in evens for o in odds])

# Step 3B: Print out your explanation of why 3A has that result

# Step 4: Print out the average of the numbers in evens using one line of code
print(sum(evens)/len(evens))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)
def minmaxmean(tuple):
  return print(f"min: {min(tuple)}, max: {max(tuple)}, mean: {sum(tuple)/len(tuple)}")

minmaxmean(odds)
minmaxmean(evens)


# Step 5B: Use print to confirm you function is working on evens and odds

# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way
