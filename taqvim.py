import calendar
a = input()
b = a.split('-')
print(calendar.month(int(b[0]), int(b[1])))