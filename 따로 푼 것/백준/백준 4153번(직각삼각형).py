import sys
input = sys.stdin.readline

while True:
    numList = sorted(list(map(int, input().split())))
    if numList == [0, 0, 0]:
        break

    if numList[2]**2 == numList[0]**2 + numList[1]**2:
        print("right")
    else:
        print("wrong")
