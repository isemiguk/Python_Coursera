now = int(input())

maxnumber = now
count = 0
while now != 0:
    if maxnumber < now:
        maxnumber = now
        count = 1
    elif maxnumber == now:
        count += 1
    now = int(input())
print(count)
