# List
a = [1, 2, 3]
print(a)

a = [1,  # item1
     2,  # item2
     3,  # item3
     4,  # item4
     5]  # item5
print(a)

# Tuple
b = (1, 2, 3)
print(b)

b = (1,  # item1
     2,  # item2
     3,  # item3
     4,  # item4
     5)  # item5
print(b)

# Dictionary
c = {"k1": 1,  # item1
     "k2": 2,  # item2
     "k3": 3}  # item3
print(c)

c = {"k1": 1,  # item1
     "k2": 2,  # item2
     "k3": 3,  # item3
     "k4": 4,  # item4
     "k5": 5}  # item5
print(c)


# function
def my_func_1(a, b, c):
    print(f"a: {a}\nb: {b}\nc: {c}")


my_func_1(1, 2, 3)


def my_func_2(a,  # used to indicate 1st arg
              b,  # used to indicate 1st arg
              c):  # used to indicate 1st arg
    print(f"a: {a}\nb: {b}\nc: {c}")


my_func_2(1, 2, 3)

a, b, c = 6, 12, 24
# Explicit statements
if a > 5 and b > 10 and c > 20:
    print("Yes")

if a > 5 \
        and b > 10 \
        and c > 20:
    print("Yes")

# String
str_1 = """this is
a string"""
print(f"str_1: {str_1}")


# Note: This case line 2 string will be intended as it looks in function description
def check_string_1():
    a = '''This is a multiline string
    string which get intended'''
    return a


print(f"check_string_1: {check_string_1()}")


# Note: This case line 2 string will not be intended as it looks in function description
def check_string_2():
    a = '''This is a multiline string
string which get intended'''
    return a


print(f"check_string_2: {check_string_2()}")
