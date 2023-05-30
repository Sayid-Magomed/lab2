year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('год', year, '- високосный')
else:
    print(year, '- это обычный год')