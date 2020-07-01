def merge(a, b):
    c = a + b
    lenght_c = len(c)
    for i in range(lenght_c-1):
        for j in range(i, lenght_c-1):
            if c[j+1] < c[i]:
                c[i], c[j+1] = c[j+1], c[i]

    return c


A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = merge(A, B)
print(*C)
