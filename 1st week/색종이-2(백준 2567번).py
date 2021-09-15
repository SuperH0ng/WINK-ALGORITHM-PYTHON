import sys

paper =[]
for i in range(102):
    paper.append([])
    
for _ in range(102):
    for u in range(102):
        paper[_].append(0)

def overlap(a,b,lst):
    for j in range(101-b, 91-b, -1):
        for k in range(a,a+10):
            lst[j][k] = 1
            
colorPaperCount = int(sys.stdin.readline().strip())

for l in range(colorPaperCount):
    x, y = map(int,sys.stdin.readline().split())
    overlap(x,y,paper)
        
perimeter = 0

# 1
for m in range(1,101):
    for w in range(1,101):
        if paper[m][w] == 1:
            if paper[m][w-1] == 0:
                perimeter += 1
                
            if paper[m][w+1] == 0:
                perimeter += 1
                
            if paper[m-1][w] == 0:
                perimeter += 1
                
            if paper[m+1][w] == 0:
                perimeter += 1

# 2
# def countPerimeter(q,p,final,count):
#     if final[q][p-1] == 0:
#         count += 1
            
#     if final[q][p+1] == 0:
#         count += 1
            
#     if final[q-1][p] == 0:
#         count += 1
            
#     if final[q+1][p] == 0:
#         count += 1
    
#     return count

# for m in range(1,101):
#     for w in range(1,101):
#         if paper[m][w] == 1:
#             perimeter = countPerimeter(m,w,paper,perimeter)                
                
print(perimeter)
