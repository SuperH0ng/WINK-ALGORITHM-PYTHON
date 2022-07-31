n = int(input())
isPrime = [False, False] + [True] * (n - 1)
prime = []

for i in range(2, n + 1) :
    if isPrime[i] == True :
        prime.append(i)
        for j in range(i*2, n + 1, i) :
            isPrime[j] = False
            
start = 0; end = 1
sum = sum(prime[start:end])
answer = 0

while start < len(prime) :
    if sum == n :
        answer += 1
    
    if sum <= n :
        try :
            sum += prime[end]
            end += 1
        except :
            break
    else :
        sum -= prime[start]
        start += 1
    
    

print(answer)
