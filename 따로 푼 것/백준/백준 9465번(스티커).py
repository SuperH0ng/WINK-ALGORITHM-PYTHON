import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc) : 
    n = int(input())
    s1 = [0, 0] + list(map(int, input().split()))
    s2 = [0, 0] + list(map(int, input().split()))

    for j in range(2, n+2) : 
        s1[j] += max(s2[j-1], s2[j-2], s1[j-2])
        s2[j] += max(s1[j-1], s2[j-2], s1[j-2])

    print(max(s1[-1], s2[-1]))