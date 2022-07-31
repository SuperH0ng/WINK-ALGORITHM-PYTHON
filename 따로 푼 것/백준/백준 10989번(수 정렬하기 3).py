import sys
input = sys.stdin.readline

N = int(input())
numList = [0] * 10001

for i in range(N) :
    num = int(input())
    numList[num] += 1

for i in range(1, 10001) :
    for j in range(numList[i]) :
        print(i)