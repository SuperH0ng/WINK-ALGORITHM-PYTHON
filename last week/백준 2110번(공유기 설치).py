import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted(list(int(input()) for i in range(N)))
maxDist = (home[-1] - home[0]) // (C - 1)
minDist = 1

def bin(count, start, end, m):
    
    mid = (start + end) // 2
    c = count
    s = home[0]
    for i in range(1, len(home)) :
        if home[i] - s >= mid :
            c -= 1
            s = home[i]
    if c > 0 :
        dist = -1
    else :
        dist = mid
    
    if start == end :
        return max(dist, m)
    
    if dist == -1 :
        return bin(count, start, mid - 1, m)
    else :
        return bin(count, mid+1, end, max(m, dist))
        

print(bin(C-1, minDist, maxDist, 1))
