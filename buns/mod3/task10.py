size = int(input())
matrix = [[str(j + 1) for _ in range(size)] for j in range(size)]

print("Матрица:")
for row in matrix:
    print(", ".join(row))

matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]

print("Транспонированная матрица:")
for row in matrix:
    print(", ".join(row))
