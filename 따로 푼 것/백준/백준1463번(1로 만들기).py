N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1) :
    div2 = N
    div3 = N
    if i % 2 == 0 :
        div2 = dp[i//2]
    if i % 3 == 0 :
        div3 = dp[i//3]
        
    dp[i] = min(dp[i-1], div2, div3) + 1
    
print(dp[-1])