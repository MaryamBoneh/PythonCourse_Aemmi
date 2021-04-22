
class Time():
    def __init__(self, h=0, m=0, s=0):
       self.h = int(h)
       self.m = int(m)
       self.s = int(s)

    def sum(self, other):
        result = Time(0,0,0)
        result.h = self.h + other.h
        result.m = self.m + other.m
        result.s = self.s + other.s

        if result.s > 60:
            result.s -= 60
            result.m += 1
        if result.m > 60:
            result.m -= 60
            result.h += 1

        return [result.h, result.m, result.s]

    def minus(self, other):
        result = Time(0,0,0)
        result.h = self.h - other.h
        result.m = self.m - other.m
        result.s = self.s - other.s

        if result.s < 0:
            result.s += 60
            result.m -= 1
        if result.m < 0:
            result.m += 60
            result.h -= 1

        return [result.h, result.m, result.s]

    def timeToSeconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def secondsToTime(self):
        time = int(input('pleas enter seconds: '))
        if(time < 60):
            print(time, "second")
        elif(time < 3600):
            print(time // 60, ":", time % 60)
        else:
            print(time // 3600, ":", ((time % 3600) // 60), ":", time % 60)


time = input('please enter time with format {hh:mm:ss}: ')
time = time.split(':')
t = Time(time[0], time[1], time[2])

while True:
    select = input(' 1- sum \n 2- minus \n 3- seconds to time \n 4- time to seconds \n 5- exit \n ')
    if select == '1':
        time = input('please enter time 2 with format {hh:mm:ss}: ')
        time = time.split(':')
        t2 = Time(time[0], time[1], time[2])
        result = t.sum(t2)
        print(result[0], ':', result[1], ':', result[2])
        
    elif select == '2':
        time = input('please enter time 2 with format {hh:mm:ss}: ')
        time = time.split(':')
        t2 = Time(time[0], time[1], time[2])
        result = t.minus(t2)
        print(result[0], ':', result[1], ':', result[2])
        
    elif select == '3':
        t.secondsToTime()
        
    elif select == '4':
        result = t.timeToSeconds()
        print(result, 'seconds')
        
    else:
        exit()
