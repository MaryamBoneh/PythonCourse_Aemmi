from date_oo import DateClass

today = input('please enter date today whith format {yyyy/mm/dd} : ')
birthDay = input('please enter your date of birth for calc your age whith format {yyyy/mm/dd} : ')

today = today.split('/')
birthDay = birthDay.split('/')

birthDayOBJ = DateClass(int(birthDay[0]), int(birthDay[1]), int(birthDay[2]))
todayOBJ = DateClass(int(today[0]), int(today[1]), int(today[2]))

if birthDayOBJ.isValidDate() and todayOBJ.isValidDate():
    age = todayOBJ.sub(birthDayOBJ)
    print('you have', age['y'], 'year and', age['m'], 'month and', age['d'], 'day')
else:
    print('input text is incorrect.')
