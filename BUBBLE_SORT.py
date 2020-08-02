def bubble_sort(list):
    length = len(list)
    for i in range(length**2):
        for k in range(1,length):
            temp = 0
            if (list[k - 1] > list[k]):
                temp = list[k]
                list[k] = list[k - 1]
                list[k - 1] = temp
                print(list)
        length -= 1
    return list
integers = []
bubble_sort(integers)
print(integers)