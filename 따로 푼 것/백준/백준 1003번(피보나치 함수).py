import sys
input = sys.stdin.readline
    
t = int(input())
case = [int(input()) for i in range(t)]
m = max(case)

countList = [1, 0, 0, 1]
idx = 2
while(idx <= m) :
    countList.append(countList[idx*2 - 4] + countList[idx*2 - 2])
    countList.append(countList[idx*2 - 1] + countList[idx*2 - 3])
    idx += 1
    
for c in case :
    print(countList[c*2], countList[c*2+ 1])
