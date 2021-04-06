n = int(input('how many row of the khayyam triangle you want? '))

khayyam_triangle = [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(1,i):
        khayyam_triangle[i][j] = khayyam_triangle[i-1][j-1] + khayyam_triangle[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(khayyam_triangle[i][j], end=' ')
    print('')

