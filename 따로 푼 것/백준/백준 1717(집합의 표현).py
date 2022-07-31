import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = [i for i in range(n+1)]

def findRoot(cur) :
    if arr[cur] == cur :
        return cur
    arr[cur] = findRoot(arr[cur])
    return arr[cur]

for i in range(m) :
    c, a, b = map(int, input().split())

    if c == 1 :
        if findRoot(a) == findRoot(b):
            print("YES")
        else :
            print("NO")
    else : # c = 0
        ar = findRoot(a)
        br = findRoot(b)
        if ar != br :
            arr[ar] = arr[br]