now = int(input())

maxnumber = 0
maxnumber2 = 0
while now != 0:
    if maxnumber < now:
        maxnumber2 = maxnumber
        maxnumber = now
    elif maxnumber2 < now:
        maxnumber2 = now
    now = int(input())
print(maxnumber2)
