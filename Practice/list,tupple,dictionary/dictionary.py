'''dict = {
    "name" : "abcd" , "age" : 3 , "branch" : "cse"
}

print(dict)
print(dict.get("name"))
print(dict.get("section" , "Not found"))

#dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

print(squares)
print("-"*30)'''


#sets
# Define a set correctly
'''num = {1, 2, 3, 4, 5, 6}

# Use set() constructor properly
set2 = set([1, 1, 3])  # duplicates are removed in sets

print(num)    # Output: {1, 2, 3, 4, 5, 6}
print(set2)   # Output: {1, 3}

# Define a set (not a list) to use set methods
s = {2, 5, 6, 9}

s.add(7)               # Adds 7 to the set
s.update([5, 6])       # Adds 5 and 6, but they're already present
s.remove(2)            # Removes 2 from the set
s.discard(10)          # Does nothing (10 not in set), no error
removed_item = s.pop() # Removes and returns an arbitrary item

print(s)               # Final state of the set
print("Removed item:", removed_item)'''


'''# Define two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union: all elements from both sets
print("Union:", a | b)
print("Union (method):", a.union(b))

# Intersection: common elements
print("Intersection:", a & b)
print("Intersection (method):", a.intersection(b))

# Difference: elements in a but not in b
print("Difference (a - b):", a - b)
print("Difference (method):", a.difference(b))

# Symmetric Difference: elements in either set, but not both
print("Symmetric Difference:", a ^ b)
print("Symmetric Difference (method):", a.symmetric_difference(b))

# Subset and Superset checks
print("Is {1, 2} a subset of a?", {1, 2} <= a)
print("Is a a superset of {1, 2}?", a >= {1, 2})

# Disjoint check: no common elements
print("Are a and {7, 8} disjoint?", a.isdisjoint({7, 8}))'''

squares = {x: x**2 for x in range(5)}
print(squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

original = {'x': 1, 'y': 2, 'z': 3}
print("original : " ,original)
inverted = {v: k for k, v in original.items()}
print("Inverted: " , inverted)
# Output: {1: 'x', 2: 'y', 3: 'z'}