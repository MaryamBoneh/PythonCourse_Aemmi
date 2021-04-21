
class DateClass():
    def __init__(self, y=None, m=None, d=None):
        self.year = y
        self.month = m
        self.day = d

    def isValidDate(self):
        if self.year > 9999 or self.year < 1 or self.month > 12 or self.month < 1 or self.day > 30 or self.day < 1:
            return False
        else:
            return True

    def show(self):
        print(self.year, '/', self.month, '/', self.day)

    def add(self, y, m, d):
        day = self.day + d
        month = self.month + m
        year = self.year + y

        if day > 30:
            day -= 30
            month += 1
        if month > 12:
            month -= 12
            year += 1

        return {'y': year, 'm': month, 'd': day}

    def sub(self, y, m, d):
        day = self.day - d
        month = self.month - m
        year = self.year - y

        if day < 1:
            day += 30
            month -= 1
        if month < 1:
            month += 12
            year -= 1
        if month == 0:
            month = 12

        return {'y': year, 'm': month, 'd': day}

    def getMonthName(self):
        months = ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']
        return months[self.month - 1]

    def isLeapYear(self):
        if self.year <= 1399:
            for y in range(1399, self.year - 1, -4):
                if self.year == y:
                    return True
            else:
                return False
        else:
            for y in range(1399, self.year + 1, 4):
                if self.year == y:
                    return True
            else:
                return False


# d = DateClass(1400, 2, 1)
# d.show()
# print(d.add(2, 12, 3))
# print(d.sub(1377, 11, 28))
# if d.isLeapYear():
#     print('is leap')
# else:
#     print('not leap')
# print(d.getMonthName())
