import random


SIZE = 3

matrix_one = [[random.randint(1,100) for j in range(SIZE)] for i in range(SIZE)]
matrix_two = [[random.randint(1,100) for j in range(SIZE)] for i in range(SIZE)]

print()
print("Первая матрица: ")
[print([matrix_one[i][j] for j in range(SIZE)], end='\n') for i in range(SIZE)]
print()

print("Вторая матрица")
[print([matrix_two[i][j] for j in range(SIZE)], end='\n') for i in range(SIZE)]
print()

print("Сумма матриц:")

matrix_sum = [[0 for j in range(SIZE)] for i in range(SIZE)]
for i in range(SIZE):
    for j in range(SIZE):
        matrix_sum[i][j] = matrix_one[i][j] + matrix_two[i][j]

[print([matrix_sum[i][j] for j in range(SIZE)], end='\n') for i in range(SIZE)]
print()
