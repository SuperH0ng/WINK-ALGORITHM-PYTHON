import sys
N = int(sys.stdin.readline())


lst = []
for _ in range(N) :
    lst.extend(list(map(int,sys.stdin.readline().split())))
    lst = sorted(lst, reverse=True)[:N]
    
print(lst[N-1])
