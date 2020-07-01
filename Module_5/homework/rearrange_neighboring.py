numbers = list(map(int, input().split()))

count_numbers = len(numbers)
for i in range(0, count_numbers, 2):
    if i == count_numbers - 1:
        print(numbers[i])
    else:
        a, b = numbers[i+1], numbers[i]
        print(a, b, end=' ')
