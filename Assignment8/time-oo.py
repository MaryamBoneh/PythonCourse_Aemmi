
class Time():
    def __init__(self, h, m, s):
        self.time1 = {'h': int(h), 'm': int(m), 's': int(s)}

    def sum(self, h, m, s):
        hour = self.time1['h'] + h
        minut = self.time1['m'] + m
        second = self.time1['s'] + s

        if second > 60:
            second -= 60
            minut += 1
        if minut > 60:
            minut -= 60
            hour += 1

        return [hour, minut, second]

    def minus(self, h, m, s):
        hour = self.time1['h'] - h
        minut = self.time1['m'] - m
        second = self.time1['s'] - s

        if second < 0:
            second += 60
            minut -= 1
        if minut < 0:
            minut += 60
            hour -= 1

        return [hour, minut, second]

    def timeToSeconds(self):
        return self.time1['h'] * 3600 + self.time1['m'] * 60 + self.time1['s']

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
        result = t.sum(int(time[0]), int(time[1]), int(time[2]))
        print(result[0], ':', result[1], ':', result[2])
        
    elif select == '2':
        time = input('please enter time 2 with format {hh:mm:ss}: ')
        time = time.split(':')
        result = t.minus(int(time[0]), int(time[1]), int(time[2]))
        print(result[0], ':', result[1], ':', result[2])
        
    elif select == '3':
        t.secondsToTime()
        
    elif select == '4':
        result = t.timeToSeconds()
        print(result, 'seconds')
        
    else:
        exit()
