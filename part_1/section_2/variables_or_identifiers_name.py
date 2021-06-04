# Must(From the PEP 8 Style Guide)
# 1. start with underscore(_) or letter(a-z A-Z)
# 1.a followed by any no of underscores(_), letters(a-z A-Z), or digits(0-9)

# 2. Cannot be reserved words:
# 2.a: None, True, False, and , or, not, if ,else, elif, for, while, break, continue, pass, def, lambda,
# 2.a: global, nonlocal, return, yield, del, in, is, assert, class, try, except, finally, raise, import,
# 2.a: from, with, as

# Conventions:
# 3. Ex: "_my_var_1" : For 'internal use' or 'private' objects.
# Note: if we import some module and the above pvt variable is inside it so it will not be imported
# ex: from module import *

# 4. Ex: "__my_var_1" : Used to mangle class attributes - useful in inheritance chains

# 5. Ex: "__my_var_1__": Used for system defined names that have a special meaning to the interpreter. Eg: "__init__", "__getattr__", "__setattr__", etc.
x = 10
y = 5
print(x.__gt__(y))  # o/p: True

# 6. For "packages": short, all-lowercase names. Preferably no underscores. Eg: 'utilities'
# 7. For "modules": short, all-lowercase names. Can have underscores. Eg: 'db_utils'
# 8. For "classes": Capital words(upper camel case) convention. Eg: 'BankAccount'
# 9. For "functions": lowercase, words seperated by underscores(snake_case). Eg: 'open_account'
# 11. For "variables": lowercase, words seperated by underscores(snake_case). Eg: 'account_id'
# 12. For "constants": all-uppercase, words separated by underscores(all cap snake_case). Eg: 'MIN_APR'
