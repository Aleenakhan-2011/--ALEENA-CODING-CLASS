n = int(input("Enter the number of rows: "))

for i in range(0, n): #outer loop for rows
    for j in range(0, i + 1): #inner loop for columns
        print("*", end=" ")

    print()