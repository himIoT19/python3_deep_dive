from math import sqrt
import math

s_list = [1, 2, 3, 4]

# Length of list s_list
len_sl = len(s_list)

print(f"Square root of list 4 = {sqrt(s_list[len_sl - 1])}")

# Value of pi
print(f"pi = {math.pi}")

# Exponential
print(f"Exponential of 1 = {math.exp(1)}")


# User function
def my_func():
    print("my_func")


print(f"{my_func}")

# function call
my_func()


def my_func_1(a: int, b: int):
    return a * b


print(f"{my_func_1}")

# function call: PASS
call_1 = my_func_1(2, 3)
print(f"my_func_1 call_1: {call_1}")

# function call: PASS
call_2 = my_func_1([2, 1], 3)
print(f"my_func_1 call_2: {call_2}")

# function call: PASS
call_3 = my_func_1('a', 3)
print(f"my_func_1 call_3: {call_3}")


# function call: FAIL
# call_4 = my_func_1('a', 'b')
# print(f"my_func_1 call_4: {call_4}")


# When to call a function
def func_3():
    return func_4()


def func_4():
    return "Running func_4..."


print(f"calling func_3: {func_3()}")


# When to not call a function
# def func_5():
#     return func_6()


# # o/p: NameError: name 'func_6' is not defined
# print(f"calling func_5: {func_5()}")


# def func_6():
#     return "Running func_6..."


# Lambda functions:
def lambda1(x):
    """
    This function is equivalent to --> lambda_1 = lambda x: x**2
    """
    return x ** 2


o_p = lambda1(5)
print(f"{o_p}")
