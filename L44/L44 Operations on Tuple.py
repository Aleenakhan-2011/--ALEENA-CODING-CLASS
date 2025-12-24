my_tuple = ()  #empty tuple
print(my_tuple)
print()

#Tuple with integers
my_tuple = (1, 2, 3)
print("tuple with integer values: ", my_tuple)

#Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4) #integer, string, float
print("tuple with mixed datatype: ", my_tuple)

#nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) # tuple consisting of string, list and another tuple
print("nested tuple: ", my_tuple)
print()

#nested tuple 
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

#nested index
print(n_tuple[0][3])  
print(n_tuple[1][2])
print()

# accessing tuple elements using indexing
my_tuple = ('b','e','a','u','t','y')
print(my_tuple[0])  
print(my_tuple[5])
print()

#iterating through a tuple
for letter in my_tuple:
    print("Hello", letter)