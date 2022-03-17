import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
b = list(map(int, input().split()))

answer = abs(n - 100)

def remoteController(target, breakButton) :
    up = ""
    down = ""
    mid = ""
    sNum = str(target)
    
    for s in sNum :
        if int(s) not in breakButton :
            mid += s
        else :
            upNum = int(s) + 1
            while (upNum in breakButton) :
                upNum += 1
            up += str(upNum)

            downNum = int(s) - 1
            while (downNum in breakButton) :
                down -= 1
            if downNum < 0 :
                continue
            down += str(downNum)