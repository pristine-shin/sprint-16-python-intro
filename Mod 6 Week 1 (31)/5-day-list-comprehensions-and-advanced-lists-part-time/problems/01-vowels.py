# Create a function that takes in a `string`. Using list comprehension, the
# function should return all of the vowels from the string.

# Write your function here.
def vowels(str):
  vowels = [c for c in str if c in 'aeiouAEIOU']
  return vowels

print(vowels("An amazing person")) #> ['A', 'a', 'a', 'i', 'e', 'o']
print(vowels("Coding is cool")) #> ['o', 'i', 'i', 'o', 'o']
print(vowels("People are NICE")) #> ['e', 'o', 'e', 'a', 'e', 'I', 'E']
