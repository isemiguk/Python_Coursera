number_list = list(map(int, input().split()))

count_positive = 0
for number in number_list:
    if number > 0:
        count_positive += 1

print(count_positive)
