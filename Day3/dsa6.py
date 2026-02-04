n = 6

def print_m(n,inverted=False):

    range_m = range(n, 0, -1) if inverted else range(1, n + 1)

    for i in range_m:
        if i == 0:
            print("*" + " " * 2 * n + "*")
        else:
            first = "*" + " " * (i - 1) + "*"
            middle = " " * (2 * (n - i))
            last = "*" + " " * (i - 1) + "*"
            print(first + middle + last)

def hollow_butterfly(n):
    print_m(n)
    print_m(n, True)

hollow_butterfly(10)


