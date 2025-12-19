def test(lst):
    result = {}
    for item in lst:
            result[item[0]] = item[1:]
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lila Smith', 'V'], [3, 'Amir Khan', 'VI'], [4, 'Sara Lee', 'VI'], [5, 'Tom Brown', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted list to dictionary:")
print(test(students))