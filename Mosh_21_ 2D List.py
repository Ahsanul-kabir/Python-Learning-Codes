
matrix = [
    [1,2,3],
    [2,3,4],
    [5,10,23]
]
print(matrix[2][2])
print('\n')
matrix[2][2] = 50
print('\n')
print(matrix[2][2])


print('\n')
for row in matrix:
    for item in row:
        print(item)