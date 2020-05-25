a = int(input())
b = int(input())
N = int(input())

sumcent = a * 100 + b

cost = sumcent * N
print(cost // 100, cost % 100, sep=' ')
