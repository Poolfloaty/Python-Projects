#Manning.com LiveProject - Python Variables
#Unit 1 Solution 1
#Author: Brent Lang
#Date: 07/15/21
#Purpose: Get an evidence-based understanding of how variables behave in Python.
#         Explore how setting two variables to the same value may (or may not) mean a deeper connection.

#Integer variables are immutable
int_a = 1
int_b = int_a
int_b = 10

#Floating Point variables are immutable
float_a = 1.1
float_b = float_a
float_b = 10.5

#String variables are immutable
string_a = "String A"
string_b = string_a
string_b = "String B"

#List variables are mutable
list_a = [10,20,30]
list_b = list_a
list_b[0] = 999
#list_b = [100,200,300]

#Tuple variables are immutable
tuple_a = (1,2,3)
tuple_b = tuple_a
tuple_b = (10,20,30)

#Dictionary variables are mutable
dict_a = {"key1": 1, "key2": 2, "key3": 3}
dict_b = dict_a
dict_b["key1"] = 999
#dict_b = {"key10": 10, "key20": 20, "key30": 30}

print(f"int_a = {int_a}\nint_b = {int_b}")
print(f"float_a = {float_a}\nfloat_b = {float_b}")
print(f"string_a = {string_a}\nstring_b = {string_b}")
print(f"list_a = {list_a}\nlist_b = {list_b}")
print(f"tuple_a = {tuple_a}\ntuple_b = {tuple_b}")
print(f"dict_a = {dict_a}\ndict_b = {dict_b}")