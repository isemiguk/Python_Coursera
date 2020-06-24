size = int(input())
number_list = list(map(int, input().split()))
number = int(input())


def buble(num_list, size):
    for i in range(size-1):
        for j in range(size-1-i): 
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

if number_list.count(number) > 0:
    min_n = number
else:
    buble(number_list, size)
    min_n = number_list[size-1]
    delta = abs(number - min_n)
    for i in range(size):
        if abs(number - number_list[i]) < abs(delta):
            min_n = number_list[i]
            delta = abs(number - number_list[i])
print(min_n)
