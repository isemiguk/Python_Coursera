N = int(input())
hour = N // 60 % 24
min = N % 60
print(hour, min, sep=' ')
