def IsPointInSquare(x, y):
    xInSquare = x <= 1 and x >= -1
    yInSquare = y <= 1 and y >= -1
    return xInSquare and yInSquare

x = float(input())
y = float(input())

if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
