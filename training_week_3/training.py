# -1-
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# pairs = list(zip(names, ages))
# print(pairs)

# for name, age in zip(names, ages):
#     print(f'{name} is {age}')

# for name, age in zip(names, ages):
#     print(name, age)

# -2-
# paired_data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# names, ages = zip(*paired_data)
# print(names, end=' \n')
# print(ages, end=' ')

# -3- Транспонирование матрицы

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transposed = list(zip(*matrix))
# print(matrix)
# print(type(matrix))
# print(transposed)
# print(type(transposed))

# transposed_matrix = [list(row) for row in zip(*matrix)]
# print(transposed_matrix)
# print(type(transposed_matrix))
