import sys
import os

class Timee():
    def __init__(self):
        self.time1 = {}
        self.time2 = {}
        self.t1 = ''
        self.t2 = ''
        
        while True:
            self.select = input(' 1- sum \n 2- minus \n 3- seconds to time \n 4- time to seconds \n 5- exit \n ')

            if self.select == '1':
                self.getTime()
                self.sum()
            elif self.select == '2':
                self.getTime()
                self.minus()
            elif self.select == '3':
                self.secondsToTime()
            elif self.select == '4':
                self.timeToSeconds()
            else:
                exit()
        
    def getTime(self):
        self.t1 = input('please enter time 1 with format {hh:mm:ss}: ')
        self.t2 = input('please enter time 2 with format {hh:mm:ss}: ')

        self.t1 = self.t1.split(':')
        self.t2 = self.t2.split(':')
        
        time1 = {'h': int(self.t1[0]), 'm': int(self.t1[1]), 's': int(self.t1[2])}
        time2 = {'h': int(self.t2[0]), 'm': int(self.t2[1]), 's': int(self.t2[2])}
        
    
    def sum(self):
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


    def minus(self):
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



if __name__ == "__main__":
    widget = Timee()
    widget.show()