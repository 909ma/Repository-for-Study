line = input().split()
x = int(line[0])
y = int(line[1])

count = 0
for month in range(x, 1, -1):
    if month == 1:
        pass
    elif month == 2:
        count += 31
    elif month == 3:
        count += 28
    elif month == 4:
        count += 31
    elif month == 5:
        count += 30
    elif month == 6:
        count += 31
    elif month == 7:
        count += 30
    elif month == 8:
        count += 31
    elif month == 9:
        count += 31
    elif month == 10:
        count += 30
    elif month == 11:
        count += 31
    elif month == 12:
        count += 30

count += y
days = count % 7

if days == 1:
    print("MON")
elif days == 2:
    print("TUE")
elif days == 3:
    print("WED")
elif days == 4:
    print("THU")
elif days == 5:
    print("FRI")
elif days == 6:
    print("SAT")
elif days == 0:
    print("SUN")
