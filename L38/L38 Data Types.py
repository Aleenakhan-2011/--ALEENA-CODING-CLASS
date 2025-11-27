name = "Alice"
age = 25
is_student = True
weight = 65.5

print("original data:")

print("Name:", name)
print("Data type of name:", type(name))
print()

print("Age:", age)
print("Data type of age:", type(age))
print()

print("Is Student:", is_student)
print("Data type of is_student:", type(is_student))
print()

print("Weight:", weight)
print("Data type of weight:", type(weight))
print()
print()

print("After type casting...")
age = str(age)
print(age)

print("Data type of age is", type(age))
print()

weight = int(weight)
print(weight)
print("Data type of weight is", type(weight))
