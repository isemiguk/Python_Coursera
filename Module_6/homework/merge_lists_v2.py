def merge(a, b):

    lenght_a = len(a)
    lenght_b = len(b)

    if lenght_a > lenght_b:
        a, b = b, a
        lenght_a, lenght_b = lenght_b, lenght_a

    i = 0
    j = 0
    c = []

    while i <= lenght_a:
        if i == lenght_a:
            c = c + b[j:lenght_b]
            return c
        elif j == lenght_b:
            c = c + a[i:lenght_a]
            return c

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] == b[j]:
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
        else:
            c.append(b[j])
            j += 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = merge(A, B)
print(*C)
