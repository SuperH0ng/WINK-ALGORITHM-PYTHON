import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leakList = sorted(list(map(int, input().split())))
cnt = 1
end = leakList[0] - 0.5 + L

i = 0
while i < N:
    if leakList[i] > end :
        end = leakList[i] - 0.5 + L
        cnt += 1
    i += 1
print(cnt)