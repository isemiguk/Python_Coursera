number_list = list(map(int, input().split()))

least = 0
for number in number_list:
    if number > 0 and (number < least or least == 0):
        least = number

print(least)
