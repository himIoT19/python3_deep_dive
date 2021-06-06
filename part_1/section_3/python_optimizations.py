# A) For Integers(int): Integer Interning
print("<--><--><--><--><--><--><--><--><--><-->")
# Example1:
a = 10
b = 10
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")

print("<--><--><--><--><--><--><--><--><--><-->")
# Example2:
a = 256
b = 256
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")

print("<--><--><--><--><--><--><--><--><--><-->")
# Example3: (try this in console)
"""
In[2]: a = 257
In[3]: b = 257
In[4]: a is b
Out[4]: False
Since:
In[5]: id(a)
Out[5]: 1874731298128
In[6]: id(b)
Out[6]: 1874731298224
"""
a = 257
b = 257
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")

print("<--><--><--><--><--><--><--><--><--><-->")
# Example4:
a = 10
b = int(10)
c = int("10")
d = int("1010", base=2)
print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
print(f"id(a) = {id(a)}\nid(b) = {id(b)}\nid(c) = {id(c)}\nid(d) = {id(d)}")

# B): For Strings(str): String Interning
print("<--><--><--><--><--><--><--><--><--><-->")
# Example1: (try in console)
"""
In[2]: a = 'hello'
In[3]: b = 'hello'
In[4]: a is b
Out[4]: True
In[5]: id(a)
Out[5]: 1707523439984
In[6]: id(b)
Out[6]: 1707523439984
"""
a = "hello"
b = 'hello'
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")

print("<--><--><--><--><--><--><--><--><--><-->")
# Example2: (Try in python console)
"""
In[1]: a = "hello world"
In[2]: b = "hello world"
In[3]: a is b
Out[3]: False
In[4]: id(a)
Out[4]: 1874731329392
In[5]: id(b)
Out[5]: 1874731344624
In[6]: a == b
Out[6]: True
"""
a = "hello world"
b = 'hello world'
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")
# Example3: (Try in python console)
"""
In[2]: a = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
In[3]: b = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
In[4]: id(a)
Out[4]: 2188061458192
In[5]: id(b)
Out[5]: 2188061458192
In[6]: a is b
Out[6]: True
In[7]: a == b
Out[7]: True
"""
a = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
b = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")
# Example4: Force String Interning (Try it on console)
"""
In[2]: import sys
In[3]: a = sys.intern('hello world!')
In[4]: b = sys.intern('hello world!')
In[5]: c = 'hello world!'
In[6]: id(a)
Out[6]: 2833233652336
In[7]: id(b)
Out[7]: 2833233652336
In[8]: id(c)
Out[8]: 2833233663920
In[9]: a is b
Out[9]: True
In[10]: a == b
Out[10]: True
In[11]: a is c
Out[11]: False
In[12]: a == c
Out[12]: True
In[13]: b is c
Out[13]: False
In[14]: b == c
Out[14]: True
"""
import sys

a = sys.intern('hello world!')
b = sys.intern('hello world!')
c = 'hello world!'
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print(f"a is b: {a is c}")
print(f"a == b: {a == c}")
print(f"b is c: {b is c}")
print(f"b == c: {b == c}")

print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")


# Example5:
def compare_using_equals(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200

    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern("a long string that is not interned" * 200)
    b = sys.intern("a long string that is not interned" * 200)

    for i in range(n):
        if a is b:
            pass


import time

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print(F"Time(compare_using_equals): {end - start}")

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print(f"Time(compare_using_interning): {end - start}")

# C: Peephole(This is another variety of optimizations that can occur at the compile time.)
print("<--><--><--><--><--><--><--><--><--><--><--><--><--><--><-->")


# Example1: (Constant expressions)
def my_func_1():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox ' * 5
    f = ['a', 'b'] * 3


print(f"my_func_1 :{my_func_1.__code__.co_consts}")


def my_func_2(e):
    if e in [1, 2, 3]:
        pass


print(f"my_func_2 :{my_func_2.__code__.co_consts}")


def my_func_3(e):
    if e in {1, 2, 3}:
        pass


print(f"my_func_3 :{my_func_3.__code__.co_consts}")

# Example2:
import string

print(f"ASCII Letters: {string.ascii_letters}")
char_list = list(string.ascii_letters)  # Ordered
print(f"Char List = {char_list}")
char_tuple = tuple(string.ascii_letters)  # Ordered
print(f"Char Tuple = {char_tuple}")
char_set = set(string.ascii_letters)  # Unordered
print(f"Char Set = {char_set}")


def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print(F"Time(membership_test using char_list): {end - start}")

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print(F"Time(membership_test using char_tuple): {end - start}")

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print(F"Time(membership_test using char_set): {end - start}")
