import sys
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
            
    return roadDic
