# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

# Write your function here.
def cap_space(str):
    result = ''
    for i in str:
        if i.islower():
            result = result + i
        else:
            result = result + " " + i

    return result.lower()

print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"
