import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
for i in range(H) :
    tomato.append([x for x in range(7)])