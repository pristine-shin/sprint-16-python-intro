# Given a set, `st`, and a list, `lst`, write a function, `add_to_set`, that
# merges the `st` to `lst` and returns the result.

# Write your code here.
def add_to_set(st, lst):
    st2 = set(lst)
    return st | st2
# could also do return st.union(st2)

st = { 1, 2, 3, 4 }
lst = [12, 4, 42, 93, 2, 85]

print(add_to_set(st, lst))    # { 1, 2, 3, 4, 42, 12, 85, 93 }
