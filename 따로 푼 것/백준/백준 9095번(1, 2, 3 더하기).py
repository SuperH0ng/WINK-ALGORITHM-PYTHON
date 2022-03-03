import sys
input = sys.stdin.readline
    
t = int(input())
case = [int(input()) for i in range(t)]
m = max(case)

dp = [0, 1, 2, 4]
idx = 4
while(idx <= m) :
    dp.append(dp[idx-3] + dp[idx-2] + dp[idx-1])
    idx += 1
    
for c in case :
    print(dp[c])
