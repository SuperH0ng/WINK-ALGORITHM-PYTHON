N = int(input())
dp = [0] * (N+1)
arr = [0, [1]]

for i in range(2, N+1) :
    div2 = N
    div3 = N
    if i % 2 == 0 :
        div2 = dp[i//2]
    if i % 3 == 0 :
        div3 = dp[i//3]
    
    minNum = min(dp[i-1], div2, div3)
    if minNum == dp[i-1] :
        arr.append(arr[i-1][:])
    elif minNum == div2 :
        arr.append(arr[i // 2][:])
    else :
        arr.append(arr[i // 3][:])
    
    arr[-1].append(i)
    dp[i] = min(dp[i-1], div2, div3) + 1
    
print(dp[-1])
for i in range(len(arr[-1]) - 1, -1, -1) :
    print(arr[-1][i], end= " ")