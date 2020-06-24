number_list = list(map(int, input().split()))

index = 0
max_number = number_list[0]
max_index = 0
for number in number_list:
    if number >= max_number:
        max_number = number
        max_index = index
    index += 1

print(max_number, max_index)
