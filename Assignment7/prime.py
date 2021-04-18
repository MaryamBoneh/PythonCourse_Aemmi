n = int(input('pleas enter first number: '))
m = int(input('pleas enter second number: '))

def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
            break
    else:
        return True

for i in range(n, m + 1):
    if isPrime(i):
        print(i, end=', ')