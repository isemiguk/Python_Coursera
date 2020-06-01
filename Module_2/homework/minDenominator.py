n = int(input())

delitel = n

i = n - 1
while i != 1:
    if n % i == 0:
        delitel = i
    i = i - 1

print(delitel)
