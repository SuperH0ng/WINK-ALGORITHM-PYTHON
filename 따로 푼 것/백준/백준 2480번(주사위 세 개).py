a, b, c = map(int, input().split())

def dice(x, y, z) :
    if x == y == z :
        return 10000 + x * 1000
    elif x == y :
        return 1000 + x * 100
    elif x == z :
        return 1000 + x * 100
    elif y == z :
        return 1000 + y * 100
    else :
        return max(a,b,c) * 100

print(dice(a,b,c))