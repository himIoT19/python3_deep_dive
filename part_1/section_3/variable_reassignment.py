# Example1:
my_va1 = 10
print(f"for my_va1={my_va1}, id = {hex(id(my_va1))}")  # 0x7fff950f07c0

my_va1 = 15
print(f"for my_va1={my_va1}, id = {hex(id(my_va1))}")  # 0x7fff950f0860, m/m addresses changed

my_va1 += 1
print(f"for my_va1={my_va1}, id = {hex(id(my_va1))}")  # 0x7fff950f0880, m/m addresses changed

b = 16
print(f"for b={b}, id = {hex(id(b))}")  # 0x7fff950f0880, m/m addresses same as my_va1
