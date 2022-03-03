def solution(dumbbell, weight):
    answer = []
    dp = [0 for i in range(weight+1)]
    dp[0] = 1
    for i in dumbbell:
        for j in range(i, weight+1):
            dp[j] = (dp[j] + dp[j-i])%1000000007
            print(dp)
    
    for i in range(weight):
        if dp[weight-i] != 0:
            answer.append(weight-i)
            answer.append(dp[weight-i])
            break
    return answer

solution([2,3], 10)
print()
solution([9, 11, 13], 32)