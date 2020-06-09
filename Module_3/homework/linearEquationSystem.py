a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

opredelitel = (a * d) - (b * c)
if opredelitel != 0:
    opredelitelX = (e * d) - (f * b)
    opredelitelY = (a * f) - (c * e)

    x = opredelitelX / opredelitel
    y = opredelitelY / opredelitel

    print(x, y)
