def sum(a, b):
    if b > 0:
        c = sum(a, b - 1)
        a = c + 1
    return a

a = int(input())
b = int(input())

print(sum(a, b))
