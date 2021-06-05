""" Changing the data inside the object is called 'modifying the internal state' of the object """
# 1. An object whose internal state can be changed is called , "Mutable".
# 2. An object whose internal state can't be changed is called , "Immutable".

# A:(Immutable): Eg:
# 1. Numbers(int, float, Booleans, etc)
# 2. Strings
# 3. Tuples Add/Remove and replace
# 4. User-Defined Classes


# B: (Mutable)
# 1. Lists
# 2. Sets
# 3. Dictionaries
# 4. User-Defined Classes

# Note:
# Example1:
# Tuples are immutable: elements can't be deleted/inserted/replaced. In this case, both the container(tuple), and all its elements (integers) are immutable
tup_1 = (1, 2, 3)
print(f"Tuple tup_1 = {tup_1}")

# Example2:
# But in this case
a = [1, 2]  # Lists are mutable: elements can be deleted/inserted/replaced
b = [3, 4]  # Lists are mutable: elements can be deleted/inserted/replaced
tup_2 = (a, b)  # tup_2 = ([1, 2], [3, 4])
print(f"Tuple tup_2 = {tup_2}")

a.append(3)
b.append(5)
print(f"After appending elements in list a, and b tuple tup_2 = {tup_2}")  # The object references in the 'tuple' didn't change but the referenced objects did mutate.

# Example3:
ml_1 = [1, 2, 3]
print(f"Type of ml_1 = {type(ml_1)}")
print(f"Base-16 id of ml_1 = {hex(id(ml_1))}")  # m/m address: 0x1e27a53b180

ml_1.append(4)
print(f"After appending, base-16 id of ml_1 = {hex(id(ml_1))}")  # m/m address: 0x1e27a53b180 not changed
print(f"After appending 4:int in list, ml_1 = {ml_1}")

# Example4:
ml_2 = [1, 2, 3]
print(f"Type of ml_2 = {type(ml_2)}")
print(f"Base-16 id of ml_2 = {hex(id(ml_2))}")  # m/m address: 0x1f6b88a0480

ml_2 = ml_2 + [4]  # New object is created: not modifying internal state
print(f"Type of ml_2 = {type(ml_2)}")
print(f"After concatenating [4], base-16 id of ml_2 = {hex(id(ml_2))}")  # m/m address: 0x1f6b88a0280 changed
print(f"After concatenating [4]:list in ml_2:list, ml_2 = {ml_2}")

# Example5:
md_1 = dict(key1=1, key2=2, key3=3)
print(f"My md_1 = {md_1}")
print(f"Base-16 id of md_1 = {hex(id(md_1))}")  # m/m address: 0x2aa8450af40

md_1['key4'] = "hello"
print(f"After adding key 'key4', md_1 = {md_1}")
print(f"After adding key 'key4', base-16 id of md_1 = {hex(id(md_1))}")  # m/m address: 0x2aa8450af40
