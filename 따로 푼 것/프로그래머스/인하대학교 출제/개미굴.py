from collections import deque
import sys
sys.setrecursionlimit(int(1e5))

def solution(road, transport):
    answer = 0
    roadList = [0]
    for r in road :
        while(max(r[0], r[1]) >= len(roadList)) :
            roadList.append(0)
            
        if roadList[r[0]] == 0  :
            roadList[r[0]] = [r[1]]
        else :
            roadList[r[0]].append(r[1])
        
        if roadList[r[1]] == 0 :
            roadList[r[1]] = [r[0]]
        else :
            roadList[r[1]].append(r[0])
    # print(roadList)

    l = len(roadList)
    parent = [0] * (l); depth = [0] * (l); c = [0] * (l)
    
    queue = deque([1])
    while queue :
        q = queue.popleft()
        c[q] = True
        
        for x in roadList[q] :
            if c[x] :
                continue
            queue.append(x)
            parent[x] = q
            depth[x] = depth[q] + 1
        
    # print(parent)
    # print(c)
    # print(depth)
    
    for t in transport :
        answer += lca(t, depth, parent)
    
    return answer
    
def lca(t, depth, parent) :
    a = t[0]; b = t[1]
    count = 0
    while depth[a] != depth[b] :
        if depth[a] > depth[b] :
            a = parent[a]
            count += 1
        else :
            b = parent[b]
            count += 1
    while a != b :
        a = parent[a]
        b = parent[b]
        count += 2
        
    return count

print(solution([[6, 3], [3, 1], [3, 2], [2, 4], [5, 1]], [[6, 3], [5, 2], [5, 4]]))