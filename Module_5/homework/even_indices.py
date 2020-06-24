number_list = list(map(int, input().split()))
even_indicies_list = number_list[::2]

for even_indicies in even_indicies_list:
    print(even_indicies, sep=' ', end=' ')
