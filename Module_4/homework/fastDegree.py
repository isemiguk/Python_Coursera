def degree(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * degree(a, n - 1)
    elif n % 2 == 0:
        return degree(a * a, n / 2)

a = float(input())
n = int(input())

print(degree(a, n))
