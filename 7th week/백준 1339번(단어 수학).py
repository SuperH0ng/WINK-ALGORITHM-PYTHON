import sys

input = sys.stdin.readline
N = int(input())
numList = sorted([input().strip() for i in range(N)], key = lambda x : len(x), reverse=True)
num = 9
wordToNum = {}
sum = 0

while len(numList[0]) > 0 :
    if numList[0][0] in wordToNum :
        sum += wordToNum[numList[0][0]] * (10**(len(numList[0])-1))
        numList[0] = numList[0][1:]
    else :
        wordToNum[numList[0][0]] = num
        sum += num * (10**(len(numList[0])-1))
        numList[0] = numList[0][1:]
        num -= 1    
    numList = sorted(numList, key = lambda x : len(x), reverse=True)
print(sum)