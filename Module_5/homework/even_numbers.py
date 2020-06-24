def even_number(number):
    return number % 2 == 0

number_list = list(map(int, input().split()))

for number in number_list:
    if even_number(number):
        print(number, sep=' ', end=' ')
