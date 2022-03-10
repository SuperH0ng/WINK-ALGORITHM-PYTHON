from math import log2

def z(y, x) :
    if y == 0 and x == 0 :
        return 1
    elif y == 0 and x == 1 :
        return 2
    elif y == 1 and x == 0 :
        return 3
    elif y == 1 and x == 1 :
        return 4

    if y == 0 :
        return ((2**int(log2(x)))**2) * 1 + z(y, x - 2**int(log2(x)))
    elif x == 0 :
        return ((2**int(log2(y)))**2) * 2 + z(y - 2**int(log2(y)), x)

    Y = int(log2(y))
    X = int(log2(x))

    if Y < X :
        return ((2**X)**2) * 1 + z(y, x - 2**X)
    elif Y > X :
        return ((2**Y)**2) * 2 + z(y - 2**Y, x)
    elif Y == X :
        return ((2**Y)**2) * 3 + z(y - 2**Y, x - 2**X)


N, r, c = map(int, input().split())

print(z(r,c) - 1)
