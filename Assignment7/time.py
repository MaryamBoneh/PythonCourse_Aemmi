time1 = {}
time2 = {}
t1 = ''
t2 = ''

def getTime():
    t1 = input('please enter time 1 with format {hh:mm:ss}: ')
    t2 = input('please enter time 2 with format {hh:mm:ss}: ')

    t1 = t1.split(':')
    t2 = t2.split(':')
    
    global time1
    global time2
    time1 = {'h': int(t1[0]), 'm': int(t1[1]), 's': int(t1[2])}
    time2 = {'h': int(t2[0]), 'm': int(t2[1]), 's': int(t2[2])}
    
    
def sum():
    h = time1['h'] + time2['h']
    m = time1['m'] + time2['m']
    s = time1['s'] + time2['s']
    
    if s > 60:
        s -= 60
        m += 1
    if m > 60:
        m -= 60
        h += 1
        
    print(h, ':', m, ':', s)


def minus():
    h = time1['h'] - time2['h']
    m = time1['m'] - time2['m']
    s = time1['s'] - time2['s']
    
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
        
    print(h, ':', m, ':', s)


def timeToSeconds():
    time = input('please enter time with format {hh:mm:ss}: ')
    time = time.split(':')
    
    print(int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]), 'second')
    

def secondsToTime():
    time = int(input('pleas enter seconds: '))
    if(time < 60):
        print(time, "second")
    elif(time < 3600):
        print(time // 60, ":", time % 60)
    else:
        print(time // 3600, ":", ((time % 3600) // 60), ":", time % 60)

while True:
    select = input(' 1- sum \n 2- minus \n 3- seconds to time \n 4- time to seconds \n 5- exit \n ')

    if select == '1':
        getTime()
        sum()
    elif select == '2':
        getTime()
        minus()
    elif select == '3':
        secondsToTime()
    elif select == '4':
        timeToSeconds()
    else:
        exit()