import sys
input = sys.stdin.readline

def primeNum(n):
    check = [True] * (n+1)
    for i in range(2, int(n ** 0.5) + 1):
        if check[i]:
            for j in range(i * 2, n, i):
                check[j] = False
    return [i for i in range(2, n+1) if check[i]]

def sosu(n, start, end) :
    i = (end + start) // 2
    if n == primeList[i] :
        return 0
    if end == i :
        if primeList[i] < n :
            return primeList[i+1] - primeList[i]
        else :
            return primeList[i] - primeList[i-1]
    elif n > primeList[i] :
        return sosu(n, i+1, end)
    else :
        return sosu(n, start, i-1)

primeList = primeNum(1299709)
T = int(input())
for n in range(T):
    print(sosu(int(input()), 0, 9999))