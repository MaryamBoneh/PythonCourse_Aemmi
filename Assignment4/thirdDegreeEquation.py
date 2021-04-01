import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))

if a != 0:
    b = b / a
    c = c / a
    d = d / a

    p = c - ((b ** 2) / 3)
    q = (2 * (b ** 3 / 27)) - (b * c) / 3 + d
    delta = ((q ** 2) / 4) + ((p ** 3) / 27)

    if delta > 0:
        print("just x1")

    elif delta == 0:
        print("x1 ,x2")

    elif delta < 0:
        print("no answer.")
else:
    exit()
