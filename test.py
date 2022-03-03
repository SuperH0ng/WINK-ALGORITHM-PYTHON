def solution(dumbbell, weight):
    dp = [0 for i in range(weight+1)]
    for d in dumbbell:
        dp[d] += 1
        for j in range(d+1, weight+1):
            dp[j] = (dp[j] + dp[j-d]) % 1000000007
            print(dp)
    idx = weight
    while (dp[idx] == 0) :
        idx -= 1
    return [idx, dp[idx]]

print(solution([2,3], 10))
print()
# print(solution([9, 11, 13], 32))
print(solution(	[1, 2, 3], 3))