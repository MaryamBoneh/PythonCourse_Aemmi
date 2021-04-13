import random

print('multiply 2 matrixs')
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))

a = [[random.randint(1, 9) for i in range(m)] for j in range(n)]
b = [[random.randint(1, 9) for i in range(k)] for j in range(m)]
result = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(m):
        for p in range(k):
            result[i][p] += (a[i][j] * b[j][p])

print('a : ', a)
print('b : ', b)
print('result : ', result)