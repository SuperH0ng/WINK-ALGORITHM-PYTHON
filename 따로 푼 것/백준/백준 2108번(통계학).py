import sys
input = sys.stdin.readline

n = int(input())
numList = sorted([int(input()) for i in range(n)])

print(round(sum(numList) / n))
print(numList[n//2])

numDic = {}
for num in numList :
    if num not in numDic :
        numDic[num] = 1
    else :
        numDic[num] += 1

mode = [0]
for num in numDic :
    if numDic[num] >= mode[0] :
            if numDic[num] == mode[0] :
                mode.append(num)
            else :
                mode = [numDic[num], num]
print(mode[1]) if len(mode) == 2 else print(mode[2])
print(numList[-1] - numList[0])