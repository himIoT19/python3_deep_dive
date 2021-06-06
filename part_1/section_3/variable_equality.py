# Memory Address: (using 'is' and 'is not' operator)
# Object State: (using '__eq__' or '==' equality and '__ne__' or '!=' un-equality operator)

# Example1:
a = 10
b = a
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

# Example2;
c = "Hello"
d = "Hello"
print(f"c is d: {c is d}")
print(f"c == d: {c == d}")

# Example3:
e = [1, 2, 3, 4, 5]
f = [1, 2, 3, 4, 5]
print(f"e is f: {e is f}")
print(f"e == f: {e == f}")  # value same

# Example4:
g = 10
h = 10.0
print(f"g is h: {g is h}")
print(f"g == h: {g == h}")  # value same

# Example5:
# "None": object can be assigned to variables to indicate that they are not set (in the way we would expect them to be), i.e. an "empty" value (or null pointer).
# But the 'None' object is a real object that is managed by PMM(Python Memory Manager). Furthermore, the m/m manager will always use a shared reference when assigning
# a variable to 'None'

i = None
j = None
k = None
print(f"i is None: {i is None}")
print(f"j is None: {j is None}")
print(f"k is None: {k is None}")
print(f"i is j: {i is j}")
print(f"i is k: {i is k}")
print(f"j is k: {j is k}")
print(f"Hexadecimal id of \ni: {hex(id(i))}\nj: {hex(id(j))}\nk: {hex(id(k))}")

# Not shared reference
l = 10 + 0j
print(f"id(l) = {id(l)}")
m = 10.0
print(f"id(m) = {id(m)}")

print(f"l is m: {l is m}")
print(f"l == m: {l == m}")
