a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if b <= a >= c:
    min1 = b
    min2 = c
elif b > c:
    min1 = a
    min2 = c
else:
    min1 = a
    min2 = b

if d >= min1 <= e or d >= min2 <= e:
    print('YES')
else:
    print('NO')
