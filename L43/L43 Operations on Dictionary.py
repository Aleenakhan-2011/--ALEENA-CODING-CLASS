dict1 =  {}

# dictionary with integer keys
dict1 = {1: 'apple',
         2: 'ball'
        }

# dictionary with mixed keys
dict2 = {'name': 'John',
            1: [2, 4, 3]
        }

# dictionary with string keys
dict3 = {'name': 'Jane',
            'age': 26,
            'phone': 156732
            }

# getting data
print(dict3['name'])
print(dict3.get('age'))
print()

# update value
print("updated dictionary 3:")
dict3['age'] = 27
print(dict3)
print()

# remove particular item
dict3.pop('age')
print("dictionary 3 after removing age:")
print(dict3)
print()

# add item
dict3['address'] = 'Surabaya'
print(dict3)
print()

# access a particular item
print("address :", dict2.get('address'))
print()

# remove all the elements
dict2.clear()
print("dictionary 2 after clearing all elements:")
print(dict2)