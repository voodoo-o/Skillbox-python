import numpy as np

# Без использования Numpy
def mult(a, b):
    n = len(a)
    m = len(b[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]

    return result


def np_mult(a, b):
    result = np.dot(a, b)

    return result


a = np.random.sample((100, 100))
b = np.random.sample((100, 100))

print("ранг a =",a.ndim, "\nранг b =", b.ndim)
print("размер матрицы a =",a.shape,"\nразмер матрицы b =",b.shape)
print(a)
print(b)