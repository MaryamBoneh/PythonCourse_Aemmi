
class Time():
    def __init__(self, n1, d1, n2, d2):
        self.time1 = {}
        self.time2 = {}
        self.t1 = ''
        self.t2 = ''
        


    def getTime(self):
        self.t1 = input('please enter time 1 with format {hh:mm:ss}: ')
        self.t2 = input('please enter time 2 with format {hh:mm:ss}: ')

        self.t1 = self.t1.split(':')
        self.t2 = self.t2.split(':')
        
        self.time1 = {'h': int(self.t1[0]), 'm': int(self.t1[1]), 's': int(self.t1[2])}
        self.time2 = {'h': int(self.t2[0]), 'm': int(self.t2[1]), 's': int(self.t2[2])}
        
        
    def sum(self):
        h = self.time1['h'] + self.time2['h']
        m = self.time1['m'] + self.time2['m']
        s = self.time1['s'] + self.time2['s']
        
        if s > 60:
            s -= 60
            m += 1
        if m > 60:
            m -= 60
            h += 1
            
        print(h, ':', m, ':', s)


    def minus(self):
        h = self.time1['h'] - self.time2['h']
        m = self.time1['m'] - self.time2['m']
        s = self.time1['s'] - self.time2['s']
        
        if s < 0:
            s += 60
            m -= 1
        if m < 0:
            m += 60
            h -= 1
            
        print(h, ':', m, ':', s)


    def timeToSeconds(self):
        time = input('please enter time with format {hh:mm:ss}: ')
        time = time.split(':')
        
        print(int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]), 'second')
        

    def secondsToTime(self):
        time = int(input('pleas enter seconds: '))
        if(time < 60):
            print(time, "second")
        elif(time < 3600):
            print(time // 60, ":", time % 60)
        else:
            print(time // 3600, ":", ((time % 3600) // 60), ":", time % 60)


t = Time()
while True:
    select = input(' 1- sum \n 2- minus \n 3- seconds to time \n 4- time to seconds \n 5- exit \n ')
    if select == '1':
        t.getTime()
        t.sum()
    elif select == '2':
        t.getTime()
        t.minus()
    elif select == '3':
        t.secondsToTime()
    elif select == '4':
        t.timeToSeconds()
    else:
        exit()