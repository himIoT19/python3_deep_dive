import ctypes
import gc


# wrapper function to get reference count
def ref_count(address: int) -> int:
    return ctypes.c_long.from_address(address).value


#
def object_by_id(object_id: int) -> str:
    for obj in gc.get_objects():
        if id(obj).__eq__(object_id):
            return "Object exists."
    return "Not found"


# Example1:
class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self: {hex(id(self))}, b: {hex(id(self.b))}")


class B:
    def __init__(self, a):
        self.a = a
        print(f"B: self: {hex(id(self))}, a: {hex(id(self.a))}")


# disable garbage collector
gc.disable()

# Create an Instance of class A
my_var1 = A()

# id of my_var1
print(f"hex(id(my_var1)) = {hex(id(my_var1))}")

# check circular reference
print(f"hex(id(my_var1.b)) = {hex(id(my_var1.b))}")
print(f"hex(id(my_var1.b.a)) = {hex(id(my_var1.b.a))}")

# Now get reference count
a_id = id(my_var1)
b_id = id(my_var1.b)
print(f"base-16 a_id = {hex(id(my_var1.b))}")
print(f"base-16 b_id = {hex(id(my_var1.b.a))}")

ref_cnt = ref_count(a_id)
print(f"Reference count for a = {ref_cnt}")

ref_cnt = ref_count(b_id)
print(f"Reference count for b = {ref_cnt}")

# Object exists or not
print(f"Object a exists: {object_by_id(a_id)}")
print(f"Object b exists: {object_by_id(b_id)}")

# Make my_var1 -> None
my_var1 = None
print(f"After my_var1 -> None, reference count for a = {ref_count(a_id)}")
print(f"After my_var1 -> None, reference count for b = {ref_count(b_id)}")

# Object exists or not(Objects not cleaned yet)
print(f"Object a exists ? {object_by_id(a_id)}")
print(f"Object b exists ? {object_by_id(b_id)}")

# Run garbage collector manually
cnt_garbage_collect = gc.collect()  # removes m/m leak
print(f"Count of garbage collect = {cnt_garbage_collect}")

# Object exists or not(Objects now cleaned)
print(f"Object a exists ? {object_by_id(a_id)}")
print(f"Object b exists ? {object_by_id(b_id)}")

# get reference count for a and b(may be other than 0: this is not object a or b. Since, objects are deleted)
print(f"After garbage collecting, reference count for a = {ref_count(a_id)}")
print(f"After garbage collecting, reference count for b = {ref_count(b_id)}")
