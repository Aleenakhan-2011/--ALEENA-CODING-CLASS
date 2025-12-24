my_set = {1, 2, 2, 3, 4, 4}  # set with integer values
print("Set :", my_set)  # Duplicates will be removed
print()

my_set2 = {"apple", "banana", "cherry"}  # set with string values
print("Set2:", my_set2)

my_set.add(5)
print("Updated Set after adding 5:", my_set)
print()

set1 = my_set
set2 = {2,4,4,6}

print("Set1", set1)
print("Set2", set2)

print("Difference from Set1 to Set2")
print(set1.difference(set2))
print()

print("Difference from Set2 to Set1")
print(set2.difference(set1))
print()

print("Symmetric Difference")
print(set1.symmetric_difference(set2))