import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

mine = []
block = n * m
for i in range(n):
    mine += list(map(int, input().split()))

max = (sum(mine) + b) // block

answer = 0
time, height = 9223372036854775807, 0
for h in range(0, max + 1) :
    for m in mine :
        if m < h :
            answer += h - m
        else :
            answer += (m - h) * 2
    if answer <= time :
        time = answer
        height = h
    answer = 0

print(time, height)