# first set
m_len = int(input('please enter length of the first set: '))
m = set()
for i in range(m_len):
    m.add(input())

# second set
n_len = int(input('please enter length of the second set: '))
n = set()
for i in range(n_len):
    n.add(input())

# showing the sets
print('m = ', m, '\tn = ', n)

# union of sets
print('union of sets: ', m | n)

# intersection of sets
print('intersection of sets: ', m.intersection(n))
