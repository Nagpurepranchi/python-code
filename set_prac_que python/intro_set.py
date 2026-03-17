"""in Python, a set is a built-in data type that is a collection of unordered, mutable, and unique elements.""" 
# Unordered: Elements have no fixed order. There is no indexing or slicing.
# Unique: The same value does not occur twice in the set.
# Mutable: We can add or remove elements. 

# create set
"""set_name = {value1, value2, value3}
print(set_name)"""

# example
"""name={1,2,3,4}
print(name)
"""
# create set to set() funcation
"""set_name = set(iterable)
print(set_name)"""

# example
"""name= set(["pranchi","preeti","mitalee"])
print(name)
"""
# create empty set
"""my_set = set()
print(my_set)"""


# add element in set
# set_name.add(element)
# example
"""name= set(["pranchi","preeti","mitalee"])
name.add("nitya")
print(name)"""


# Add multiple elements in set
"""names = {"pranchi", "nitya"}
names.update(["riya", "sonam", "neha"])
print(names)"""


# Remove element from set  with error(not safe)
"""names = {"pranchi", "nitya", "riya"}
names.remove("riya")
print(names)
"""
#  Remove element from set  without error
"""names = {"pranchi", "nitya"}
names.discard("riya")   
print(names)"""

# remove duplicate elements(Does not print duplicate values)
"""names = {"pranchi", "nitya", "nitya"}
print(names)"""

# Set operations (mathematical operations jaise union, intersection, difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        
print(a.intersection(b))  
print(a.difference(b))    
print(a.symmetric_difference(b)) 