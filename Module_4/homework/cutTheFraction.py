import math


def ReduceFraction(n, m):
    div = math.gcd(n, m)
    return n // div, m // div

n = int(input())
m = int(input())

p, q = ReduceFraction(n, m)

print(p, q)
