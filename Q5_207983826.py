# https://stackoverflow.com/questions/17310051/fibonacci-rabbits-dying-after-arbitrary-of-months

# recursionnnnn
def Alive(A):
    n = A[0]
    c = A[1]
    m = A[2]
    o = A[3]

    # base
    if (n <= 0 or c > n):
        return 0

    if (n == c):
        return 1

    # Living
    if (n <= c + m + o):
        return Alive([n - 1, c, m, o]) + Alive([n - 2, c, m, o])

    # Dead now
    elif (n == c + m + o + 1):
        return Alive([n - 1, c, m, o]) + Alive([n - 2, c, m, o]) - 1

    # quantity = fibonacci - dead and their children
    else:
        return Alive([n - 1, c, m, o]) + Alive([n - 2, c, m, o]) - Alive([n - (c + m + o + 1), c, m, o]) - 1

# run example
if __name__ == '__main__':
    print(Alive([1, 1, 5, 1]))
    print(Alive([2, 1, 5, 1]))
    print(Alive([3, 1, 5, 1]))
    print(Alive([4, 1, 5, 1]))
    print(Alive([5, 1, 5, 1]))
    print(Alive([6, 1, 5, 1]))
    print(Alive([7, 1, 5, 1]))
    print(Alive([8, 1, 5, 1]))
    print(Alive([9, 1, 5, 1]))
    print(Alive([10, 1, 5, 1]))

    print(Alive([10, 5, 7, 1]))