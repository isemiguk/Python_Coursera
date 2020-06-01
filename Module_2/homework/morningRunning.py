X = int(input())
Y = int(input())

day = 1
distance = X

while distance < Y:
    distance = distance + distance * 0.1
    day = day + 1

print(day)
