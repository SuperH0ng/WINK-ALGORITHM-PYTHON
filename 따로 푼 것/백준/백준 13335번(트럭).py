from queue import Queue

num, length, maxWeight = map(int, input().split())
truck = list(map(int, input().split()))[::-1]

bridge = Queue()
for i in range(length) :
    bridge.put(0)
time = length
weight = 0

while truck :
    weight -= bridge.get()
    if weight + truck[-1] <= maxWeight :
        t = truck.pop()
        weight += t
        bridge.put(t)
    else :
         bridge.put(0)
    time += 1

print(time)