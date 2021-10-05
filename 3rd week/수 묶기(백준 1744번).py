import sys
input = sys.stdin.readline

N = int(input()) -1
arr = sorted(list(int(input()) for _ in range(N+1)))
answer = 0
x = 0

while(x < N):
    if arr[x] < 0:
        if arr[x+1] < 0:
            answer += arr[x]*arr[x+1]
            x += 2
        elif arr[x+1] == 0 :
            x += 2
            break
        else :
            answer += arr[x]
            x += 1
            break
    elif arr[x] == 0 :
        x += 1
        break
    else :
        break

while (N > x):
    if arr[N]*arr[N-1] > arr[N]+arr[N-1]:
        answer += arr[N]*arr[N-1]
        N -= 2
    else :
        break

answer += sum(arr[x:N+1])
print(answer)