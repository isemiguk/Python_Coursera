now = int(input())

number = now
count = 0
maxcount = 0

while now != 0:
    if number == now:
        count += 1
    else:
        number = now
        if maxcount < count:
            maxcount = count
        count = 1
    if maxcount < count:
        maxcount = count
    now = int(input())
print(maxcount)
