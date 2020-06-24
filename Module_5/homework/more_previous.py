number_list = list(map(int, input().split()))

previous = number_list[0]
for number in number_list:
    if number > previous:
        print(number, sep=' ', end=' ')
    previous = number
