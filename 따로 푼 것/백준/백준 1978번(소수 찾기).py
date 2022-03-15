import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

maxNum = max(lst)
isPrime = [False, False] + [True] * (maxNum - 1)

for i in range(2, int(maxNum**0.5) + 1) :
    if isPrime[i] == True :
        for j in range(i*2, maxNum + 1, i) :
            isPrime[j] = False

answer = 0

for num in lst :
    if isPrime[num] == True :
        answer += 1

print(answer)