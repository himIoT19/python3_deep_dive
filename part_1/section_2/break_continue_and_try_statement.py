# Example1:
# try...except...finally
a = 10
b = 0
try:
    o_p = a / b
    print(f"o/p: {o_p}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This always execute")

# Example2:
print("*******************************Example2*******************************")
a = 0
b = 2

while a < 4:
    print(f"-----------------")
    a += 1
    b -= 1

    try:
        o_p = a / b
        print(f"o/p: {o_p}")
    except ZeroDivisionError as e:
        print(f"Error in {a} / {b}: {e}")
        continue
    finally:
        print(f"{a}, {b} - always execute")

    print(f"{a}, {b} - main loop")

# Example3:
print("*******************************Example3*******************************")
c = 0
d = 10

while c < 4:
    print(f"-----------------")
    c += 1
    d -= 1

    try:
        o_p = c / d
        print(f"o/p: {o_p}")
    except ZeroDivisionError as e:
        print(f"Error in {c} / {d}: {e}")
        break
    finally:
        print(f"{c}, {d} - always execute")

    print(f"{c}, {d} - main loop")
else:
    print("Code executed without a ZeroDivisionError")
