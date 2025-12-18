fruit_List = ['apple', 'banana', 'cherry', 'date', 'mango']
list_size = len(fruit_List)

print("Length of list:", list_size)
print("First element:", fruit_List[0])
print("Last element:", fruit_List[-1])

#add papaya on the last element
fruit_List.append('papaya')
print("Updated list after adding papaya:", fruit_List)
print()

#add strawberry between banana and cherry
fruit_List.insert(2, 'strawberry') #number 2 is the index number(position) 
print("Updated list after adding strawberry:", fruit_List)
print()

#remove date 
fruit_List.remove('date')
print("Updated list after removing date:", fruit_List)
print()

#remove element on index 1 
fruit_List.pop(1)
print("Updated list after removing element on index 1:", fruit_List)
print()

#sorting the list
fruit_List.sort()
print("Sorted list:", fruit_List)
print()

#reverse the list
fruit_List.reverse()
print("Reversed list:", fruit_List)
print()

print("Multiplying on list:", fruit_List * 2)
print()

fruit_List = fruit_List[:4]
print("Sliced list:", fruit_List)
print()

fruit_List.clear()
print("Updated list:", fruit_List)