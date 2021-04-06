print('------ FIBONACCI ------')

n = int(input('how many elements of the fibonacci series you want? '))
a = 0
b = 1
fibo_list = list()

for i in range(n):
    fibo_list.append(a)
    temp = a + b
    b = a
    a = temp

fibo_tuple = tuple(fibo_list)
print(fibo_tuple)
