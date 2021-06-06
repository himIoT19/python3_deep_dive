print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")
# Example1:
a = 10
print(f"Type of a : {type(a)}")

b = int(10)
print(f"Type of b : {type(b)}")

print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")
# Example2: # Get help
help(int)

print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")
# Example3:
c = int()
print(f"Value of c = {c}")

c = int('101', base=2)  # Binary: "101" -> Decimal: "5"
print(f"Value of c = {c}")

# Example4:
print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")


def square(a):  # 'square' is name of function
    return a ** 2


print(f"Type of 'square': {type(square)}")
print(f"Hexadecimal id of 'square': {hex(id(square))}")

f = square
print(f"Type of 'f': {type(f)}")
print(f"Hexadecimal id of 'f': {hex(id(f))}")
print(f"f is square: {f is square}")

# call function
result = square(3)
print(f"result: square(3) = {result}")
result = f(3)
print(f"result: f(3) = {result}")

# Example5: (return function from a function)
print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(f"Type of 'f': {type(f)}")
print(f"Hexadecimal id of 'f': {hex(id(f))}")
print(f"f is square: {f is square}")
result = f(3)
print(f"result: f(3) = {result}")

g = select_function(2)
print(f"Type of 'g': {type(g)}")
print(f"Hexadecimal id of 'g': {hex(id(g))}")
print(f"g is cube: {g is cube}")
result = g(3)
print(f"result: g(3) = {result}")

h = select_function(1)(5)
print(f"select_function(1)(5): h = {h}")

i = select_function(2)(5)
print(f"select_function(2)(5): i = {i}")

# Example6: (function passed to a function)
print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")


def execute_function(fn, n):
    return fn(n)


j = execute_function(cube, 8)
print(f"execute_function(cube, 8): j = {j}")
k = execute_function(square, 12)
print(f"execute_function(square, 12): k = {k}")
