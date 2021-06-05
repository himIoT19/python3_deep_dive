# Python M/m Manager handles reference counting

import sys

# Example1:
my_var1 = [1, 2, 3]
print(f"id(my_var1) = {id(my_var1)}")  # m/m address base-10
ref_count_1 = sys.getrefcount(my_var1)  # always expect + 1
print(f"Reference count using 'sys' module : {ref_count_1}")

# Example2:
import ctypes


# wrapper function to get reference count
def ref_count(address: int) -> int:
    return ctypes.c_long.from_address(address).value


ref_count2 = ref_count(id(my_var1))  # id() works first and released so refcount will be 1
print(f"Reference count using 'ctypes' module : {ref_count2}")

# example3:
my_var2 = my_var1
ref_count2 = ref_count(id(my_var1))  # id() works first and released so refcount will be 1
print(f"Reference count using 'ctypes' module : {ref_count2}")

# example4:
my_var3 = my_var1
ref_count2 = ref_count(id(my_var1))  # id() works first and released so refcount will be 1
print(f"Reference count using 'ctypes' module : {ref_count2}")

# example5:
my_var3 = 10
ref_count2 = ref_count(id(my_var1))  # id() works first and released so refcount will be 1
print(f"Reference count using 'ctypes' module : {ref_count2}")

# example6:
my_var2 = None
ref_count2 = ref_count(id(my_var1))  # id() works first and released so refcount will be 1
print(f"Reference count using 'ctypes' module : {ref_count2}")

# example7:
id_my_var1 = id(my_var1)
my_var1 = None
ref_count2 = ref_count(id_my_var1)  # id() works first and released so refcount will be 1

for i in range(5):
    print(f"Reference count using 'ctypes' module : {ref_count2}")

# Note: In python it dangerous to work with memories
