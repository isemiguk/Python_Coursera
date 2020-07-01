numbers = list(map(int, input().split()))

min_number = numbers[0]
max_number = numbers[0]

min_pos = 0
max_pos = 0

count_numbers = len(numbers)
for i in range(count_numbers):
    if min_number > numbers[i]:
        min_number = numbers[i]
        min_pos = i

    if max_number < numbers[i]:
        max_number = numbers[i]
        max_pos = i

numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]
print(*numbers)
