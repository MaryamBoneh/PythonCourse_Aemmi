row = int(input('number of row: '))
col = int(input('number of col: '))

for i in range(row):
    for j in range(col):
        if (i + j) % 2 == 0:
            print('#', end=' ')
        else:
            print('*', end=' ')
    print()
