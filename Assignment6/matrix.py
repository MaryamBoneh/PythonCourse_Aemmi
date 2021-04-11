import random

print('multiply 2 matrixs')
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))

a =  [[1 for i in range(m)] for j in range(n)]
b = [[1 for i in range(k)] for j in range(m)]
result = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1,9)
        
for i in range(m):
    for j in range(k):
        b[i][j] = random.randint(1,9)
       
for i in range(n):
    for j in range(k):
        for k in range(m):
            result[i][j] += (a[i][k] * b [k][j]) 
        
print('a : ', a)
print('b : ', b)
print('result : ', result)

