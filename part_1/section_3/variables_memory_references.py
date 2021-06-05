"""
# Memory references
# what variables are
# memory management
# reference counting and garbage collection
# dynamic vs static typing
# mutability and immutability
# shared references
# variable equality
# everything is an object"""

# "id()": used to find out the memory address in base-10 referenced by a variable, eg: id(var_1). We can use "hex()" to convert base-10 to hexadecimal.

# Example1:
my_var_1 = 10  # created variable
print(f"my_var_1 = {my_var_1}")
print(f"Base-10: id(my_var_1) = {id(my_var_1)}")     # get m/m reference in base-10
print(f"Hexadecimal: id(my_var_1) = {hex(id(my_var_1))}")     # get m/m reference in hexadecimal

# Example2:
greeting = "hello"
print(f"greeting = {greeting}")
print(f"Base-10: id(greeting) = {id(greeting)}")     # get m/m reference in base-10
print(f"Hexadecimal: id(greeting) = {hex(id(greeting))}")     # get m/m reference in hexadecimal
for char in greeting:
    print(f"Base-10: id({char}) = {id(char)}")  # get m/m reference in base-10
    print(f"Hexadecimal: id({char}) = {hex(id(char))}")  # get m/m reference in hexadecimal