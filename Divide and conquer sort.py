def bubble_sort(list):
    n = len(list) - 1
    outer_for_loop = 0
    inner_for_loop = 0
    for i in range(n**2):
        for i in range(n):
            temp = 0
            if list[i-1] > list[i ]:
                temp = list[i-1]
                list[i - 1] = list[i]
                list[i] = temp
            print(i)
            inner_for_loop = inner_for_loop + 1
        n = n - 1
    outer_for_loop = outer_for_loop + 1
    print("\n\nBUBBLE SORT SORTED LIST",list)
    print("outer for loop count",outer_for_loop)
    print("inner for loop count",inner_for_loop)
def divide_and_conquer(list):