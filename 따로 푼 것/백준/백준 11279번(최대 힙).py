import sys
import heapq

input = sys.stdin.readline

t = int(input())
heap = []
for i in range(t) :
    ipt = int(input())
    if ipt > 0 :
        heapq.heappush(heap, -ipt)
    else :
        if heap :
            print(">>",-heapq.heappop(heap))
        else :
            print(">>",0)