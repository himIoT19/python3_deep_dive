# Example1:
i = 0  # if, i = 5 ; the loop does not run a single time
while i < 5:  # when i = 5; the loop terminates
    print(i)
    i += 1

# Example2:
b = 12
while True:
    print(b)
    if b >= 12:
        break

# Example3:
min_len = 3

while True:
    name = input("Please enter your name: ")
    if (len(name) >= min_len and name.isprintable() and name.isalpha()):
        break

print(f"Hello, {name} :)")

# Example4:
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(f"{a}")

# Example5:
list_1 = [1, 2, 3]  # [1, 10, 2, 3]
val = 10

found = False
idx = 0

while idx < len(list_1):
    if list_1[idx] == val:
        found = True
        print(f"Found {val} in list_1 at index: {idx}")
        break
    print(f"{val} not found at list_2[{idx}]")
    idx += 1

if not found:
    list_1.append(val)

print(f"list_1: {list_1}")

# Example6:
list_2 = [1, 2, 3]  # [1, 2, 10, 3]
val = 10
idx = 0

while idx < len(list_2):
    if list_2[idx] == val:
        print(f"Found {val} in list_1 at index: {idx}")
        break
    print(f"{val} not found in list_2")
    idx += 1

else:
    list_2.append(val)

print(f"list_2: {list_2}")

