import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))
visibleBuildings = [2 for _ in range(N)]
visibleBuildings[0] -= 1
visibleBuildings[N-1] -= 1

canSee = True

def canYouSeeTheBuliding(lst,a,b):
    global canSee
    gradient = (lst[b] - lst[a]) / (b-a)
    
    for i in range(a+1,b):
        if lst[a]+(gradient*(i-a)) <= lst[i]:
            canSee = False
            break

for x in range(N-2):
    for y in range(x+2, N):
        canYouSeeTheBuliding(buildings, x, y)
        
        if canSee == True :
            visibleBuildings[x] += 1
            visibleBuildings[y] += 1
            
        else :
            canSee = True

print(max(visibleBuildings))