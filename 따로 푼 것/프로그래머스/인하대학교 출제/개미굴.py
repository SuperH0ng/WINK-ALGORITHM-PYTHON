from collections import deque

def solution(road, transport):
    answer = 0
    roadDic = {}
    for r in road :
        if r[0] not in roadDic :
            roadDic[r[0]] = [r[1]]
        else :
            roadDic[r[0]].append(r[1])
        
        if r[1] not in roadDic :
            roadDic[r[1]] = [r[0]]
        else :
            roadDic[r[1]].append(r[0])
    print(roadDic)
    for t in transport :
        answer += count(roadDic, t)
        print(answer)
        
    return answer

def count(dic, trans) :
    dest = trans[1]
    queue = deque([trans])
    cnt = 0

    while queue :
        x, y= queue.popleft()
        print(x,y)
        if x not in dic :
            return -1
        if dest in dic[x] :
            return cnt + 1
        
        for i in range(len(dic[x])) :
            for j in range(len(dic[dic[x][i]])) :
                queue.append([dic[x][i], dic[dic[x][i]][j]])
        cnt += 1
    
    return cnt

print(solution([[6, 3], [3, 1], [3, 2], [2, 4], [5, 1]], [[6, 3], [5, 2], [5, 4]]))