# Example1: When working with 'mutable' objects we have to be more careful
list_1 = [1, 2, 3]
print(f"list_1 hex id = {hex(id(list_1))} and list_1 = {list_1}")
list_2 = list_1
print(f"list_2 hex id = {hex(id(list_2))} and list_2 = {list_2}")
list_2.append(100)
# So the list_1 is also modified since both share same object reference
print(f"After appending element in list_2:\nlist_2 hex id = {hex(id(list_2))}, and list_2 = {list_2}\nlist_1 hex id = {hex(id(list_1))}, and list_1 = {list_1}")

# Example2: With 'mutable' objects, the PMM will never create shared references
list_a = [1, 2, 3]  # m/m: 0x22fca190180
print(f"list_a hex id = {hex(id(list_a))} and list_a = {list_a}")

list_b = [1, 2, 3]  # m/m: 0x22fca34b200
print(f"list_b hex id = {hex(id(list_b))} and list_b = {list_b}")

list_b.append("hello")
print(f"After appending element in list_b:\nlist_b hex id = {hex(id(list_b))}, and list_b = {list_b}\nlist_a hex id = {hex(id(list_a))}, and list_a = {list_a}")
