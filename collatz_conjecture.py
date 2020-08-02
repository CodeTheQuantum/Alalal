def collatz(num):
    steps = 0
    print(num)
    while num != 1: 
        if num%2 == 0:
            steps += 1
            num = num//2
            print(num)
        else:
            steps += 1
            num = 3*num + 1
            print(num)
    return num, steps
i = 27
print(collatz(i))