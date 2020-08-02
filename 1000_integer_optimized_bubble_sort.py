def bubble_sort(list):
    n = len(list) - 1
    outer_for_loop = 0
    inner_for_loop = 0
    for i in range(n**2):
        for i in range(n):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i] 
            print("\n",i)
            inner_for_loop = inner_for_loop + 1
        n -= 1
    outer_for_loop = outer_for_loop + 1
    print("\n\n\nBUBBLE SORT SORTED LIST",list)
    print("outer for loop count",outer_for_loop)
    print("inner for loop count",inner_for_loop)
integers = [0, -5, -4, 1, -8, 3, 2, 8, -1, 4, -7, 7, 6, -9, 9, 5, 10, -2, -10, -3]
bubble_sort(integers)