n = int(input())
isPrime = [False, False] + [True] * (n - 1)

for i in range(2, int(n**0.5) + 1) :
    if isPrime[i] == True :
        for j in range(i*2, n + 1, i) :
            isPrime[j] = False

print(isPrime)