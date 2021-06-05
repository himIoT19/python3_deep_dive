# Example1:(strings)
def modify_string(s):
    print(f"Initial s = {s} has base-16 id = {hex(id(s))}")
    s = s + " world"
    print(f"Final s = {s} has base-16 id = {hex(id(s))}")


my_str1 = "Hello"
print(f"my_str1  = {my_str1} hase base-16 id = {hex(id(my_str1))}")

modify_string(my_str1)


# Example2:(lists)
def modify_list(l):
    print(f"Initial l = {l} has base-16 id = {hex(id(l))}")
    l.append("world")
    print(f"Final l = {l} has base-16 id = {hex(id(l))}")


my_lst1 = [1, "I love python", 23.4, 'c']
print(f"my_lst1  = {my_lst1} hase base-16 id = {hex(id(my_lst1))}")

modify_list(my_lst1)


# Example3:(tup)
def modify_tuple(t):
    print(f"Initial t = {t} has base-16 id = {hex(id(t))}")
    t[0].append("world")  # taking first element of tuple is list
    print(f"Final t = {t} has base-16 id = {hex(id(t))}")


my_tup1 = ([1, "I love python", 23.4, 'c'], "ABCD")
print(f"my_tup1  = {my_tup1} hase base-16 id = {hex(id(my_tup1))}")

modify_tuple(my_tup1)
