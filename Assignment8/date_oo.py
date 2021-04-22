
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

    def add(self, other):
        result = DateClass(None, None, None)
        result.day = self.day + other.day
        result.month = self.month + other.month
        result.year = self.year + other.year

        if result.day > 30:
            result.day -= 30
            result.month += 1
        if result.month > 12:
            result.month -= 12
            result.year += 1

        return {'y': result.year, 'm': result.month, 'd': result.day}

    def sub(self, other):
        result = DateClass(None, None, None)
        result.day = self.day - other.day
        result.month = self.month - other.month
        result.year = self.year - other.year

        if result.day < 1:
            result.day += 30
            result.month -= 1
        if result.month < 1:
            result.month += 12
            result.year -= 1
        if result.month == 0:
            result.month = 12

        return {'y': result.year, 'm': result.month, 'd': result.day}

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
# if d.isLeapYear():
#     print('is leap')
# else:
#     print('not leap')
# print(d.getMonthName())
