import sys
input = sys.stdin.readline

for i in range(3) :
    n = int(input())

    x = sum(int(input()) for l in range(n))
    if x == 0 :
        print(0)
    elif x > 0 :
        print("+")
    else :
        print("-")
