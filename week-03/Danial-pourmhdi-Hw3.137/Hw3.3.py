import array
from array import array


def bubble_sort(list_of_lists):
    n = len(list_of_lists)
    for i in range(n):
        for j in range( n - i - 1):
            if list_of_lists[j] > list_of_lists[j + 1]:
                list_of_lists[j], list_of_lists[j + 1] = list_of_lists[j + 1], list_of_lists[j]

    return list_of_lists

my_list = [5, 1, 4, 2, 8]
print(bubble_sort(my_list))