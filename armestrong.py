num = int(input())
num_len = len(str(num))
print('num len: ', num_len)
temp_num = num
sum = 0

while num > 0:
    sum += ((num % 10) ** num_len)
    num = num // 10

if sum == temp_num:
    print('is Armestrong')
else:
    print('not Armestrong')
