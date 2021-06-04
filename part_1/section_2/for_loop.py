""" In Python, an 'Iterable' is an object capable of returning values one at a time. Iterable can be indexed, but 'set' is an iterable but can't be indexed. """

# Example1:
for i in range(5):  # 'range' is an iterable object
    print(i)
print("*******************************************")

# Example 2:
for i in [1, 2, 3, 4, 5]:
    print(i)
print("*******************************************")

# Example3:
for char in "Himanshu":
    print(char)
print("*******************************************")

# Example4:
for item in ("mars", 2, 'v', 4, 5):
    print(item)
print("*******************************************")

# Example5:
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
print("*******************************************")

# Example6:
for i in range(5):
    if i == 3:  # skips 3
        continue
    print(i)
print("*******************************************")

# Example7:
for i in range(5):
    if i == 3:  # stops at 3
        break
    print(i)
print("*******************************************")

# Example8:
# for i in range(1, 5):   # range(1, 10)
for i in range(1, 10):  # range(1, 5)
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found")
        break
else:
    print("No multiples of 7 in the range")
print("*******************************************")

# Example9:
for i in range(5):
    print("------------------------")
    try:
        print(10 / (i - 3))
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        continue
    finally:
        print("Always run")

    print(i)
print("*******************************************")

# Example10:
s = "hello"
i = 0
for char in s:
    print(f"Index: {i} and Value: {char}")
    i += 1
print("*******************************************")

# Example11:
s = "dimello"
for i in range(len(s)):
    print(f"Index: {i} and Value: {s[i]}")
print("*******************************************")

# Example12:
s = "khello"
for i, v in enumerate(s):  # 'enumerate' gives index and its value(as tuple).
    print(f"Index: {i} and Value: {v}")
print("*******************************************")
