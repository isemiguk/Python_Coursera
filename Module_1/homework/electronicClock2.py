N = int(input())

hour = N // 3600 % 24

minute = (N // 60 - (hour * 60)) % 60
strminute = str(minute // 10) + str(minute % 10)

sec = N % 60
strsec = str(sec // 10) + str(sec % 10)

print(hour, strminute, strsec, sep=':')
