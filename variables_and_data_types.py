# Author: Nazrul Ismail
# Description: Template code for live demo of Python Basics (Var, data types and operators)
# Values are intentionally left None. Will be replaced during live coding.
"""
    This is a multi-line comment 
"""
# Single line comment

# === Scalar Objects Types ===
# === Numeric ===
integer_var = 175546
float_var = 3.1412

# Open operators.py 

# === Boolean ===
bool_var = False
bool_var_t = True# always uppercase on first letter

# === None type ===
none_var = None

# === Strings ===
# Single or double quoated is still str
hi = "hello"
name = 'anya'
greet = hi + name 
greeting = hi + " " + name

#do some operations on string as defined in Python docs
silly = hi + " " + name * 3
print(silly)
s = "abc"

#in-built functions for str 
print("Length of s: ", len(s))

a = "apple"
b = "orange"

#Slicing -> [start:stop:step]
#start: The index of the starting element (inclusive).
#stop: The index of the stopping element (exclusive).
#step: The interval between elements to include in the slice.
print(a[0])
print()

#operators with <, >, == on strs
print(a < b)

# === Typecasting ===
int_str = None
typecast_int = None
print(int_str, type(int_str))
print(typecast_int, type(typecast_int))

# === Sequence Types ===
list_var = [1, "Anya", 'hi', 3.142]
# Accessing a list element
print(list_var[0])
# Slicing a list, e.g., from index 0 to 2
# caveat: does not include the last index i.e., 2
print(list_var[0:2])
print(list_var[::-1])
print(len(list_var))

tuple_var = (123, 12.4, "str", 'hello', 4j)
print(tuple_var)
# Inherits the same properties as lists for accessing elements and slicing
# However, it is not immutable! i.e., elements cannot be changed
print(tuple_var[0], tuple_var[0:10])
print(tuple_var[0:2])
print(tuple_var[::-1])
print(len(tuple_var))

#diff bet list and tuples
#list is mutable (it can be changed)
#tuples is immutable (fixed)
list_var[0] = "Hello"
print(list_var)


"""
range(a, b) - often used in conjunction with loops, list comprehensions, and other scenarios where iterating over
a range of numbers is required.
"""
range_var = None  # represents a sequence [1, 2, 3, 4, 5, 6]
# print([x for x in range_var])

# === Mapping type ===
# Represented as { key : value }
dictionary_var = {5 : "John Doe", 12 : "Anya", 90 : "Jaidi", 5: "hello"}
dictionary_var["key"] = None
print(dictionary_var)

#accessing elements in dictionary
for x, v in dictionary_var.items():
    print(f"keys: {x}, Values: {v}")

# Printing the values of variables to verify their data types
"""
print("Integer Variable:", integer_var, type(integer_var))
print("Float Variable:", float_var, type(float_var))
print("String Variable:", name, type(name))
print("Boolean Variable:", bool_var, type(bool_var))
print("List Variable:", list_var, type(list_var))
print("Tuple Variable:", tuple_var, type(tuple_var))
print("Range Variable:", range_var, type(range_var))
print("Dictionary Variable:", dictionary_var, type(dictionary_var))
print("None Variable:", none_var, type(none_var))
"""