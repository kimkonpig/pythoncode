import sys

array = []
for i in range(0, 9):
    array.append(int(input()))

print(max(array))
print(array.index(max(array))+1)