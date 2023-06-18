import re

arr = []
# This arr is to store the lines of a file

file = open("lc.txt", 'r')

for line in file:
    arr.append(line)


def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed "+element)

    return new_array


arr = remove_elements_with_pattern(arr, "/solution")

arr = list(set(arr))
print(len(arr))

with open('lc_problems.txt', 'a') as f:
    for j in arr:
        f.write(j)
