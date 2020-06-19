def power(a, n):
    if n > 1:
        extent = power(a, n - 1) * a
        return extent
    elif n == 0:
        return 1
    else:
        return a

a = float(input())
n = int(input())

print(power(a, n))
