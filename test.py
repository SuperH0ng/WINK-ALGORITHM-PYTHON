import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted(list(int(input()) for i in range(N)))
maxDist = (home[-1] - home[0]) // (C - 1)
minDist = 1

def wifi(count, dist):
    start = home[0]
    for i in range(1, len(home)):
        if home[i] - start >= dist :
            count -= 1
            start = home[i]
    
    if count > 0 :
        return -1
    return dist

def bin(count, start, end, m):
    
    # mid = (start + end) // 2
    
    
    
    
    
    
    
    
    
    mid = (start + end) // 2
    # dist = wifi(count, mid)
    c = count
    
    s = home[0]
    for i in range(1, len(home)):
        if home[i] - s >= mid :
            c -= 1
            s = home[i]
    if c > 0 :
        dist = -1
    else :
        dist = mid
    
    if start == end :
        return max(m, dist)
    if dist == -1 :
        return bin(count, start, mid-1, m)
    else :
        return bin(count, mid+1, end, max(m, dist))
        

print(bin(C-1, minDist, maxDist, 1))
