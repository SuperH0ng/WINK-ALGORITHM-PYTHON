# def solution(company):
#     child = list([] for i in range(len(company)))
#     parent = list([] for i in range(len(company)))
#     time = list([] for i in range(len(company)))
#     for i in range(1, len(company)) :
#         parent[i].append(company[i])
#         child[company[i]].append(i)
#     print(child)
#     print(parent)
    
#     for j in range(len(company)) :
        
    
#     answer = 0
#     return answer

# solution([-1, 0, 0, 1, 3])




# class NODE:
#     def __init__(self, number):
#         self.num = number
#         self.time = 0
#         self.child = []
#         self.visited = False
        
#     def __repr__(self) :
#         return str(self.num)
        
#     def addChild(self, child):
#         self.child.append(child)
        
#     def DFS(self):
#         if self.visited == True:
#             return 0
#         self.visited = True
#         #print(self.num , " ")
#         time = []
#         if len(self.child) == 0:
#             return 0
#         for c in self.child:
#             time.append(c.DFS())
#         time.sort()
#         for i in range(len(time)):
#             time[i] += len(time)-i
#         self.time = max(time)
#         return self.time

# def solution(company):
#     nodes = []
#     for i in range(len(company)):
#         if i == 0:
#             parent = NODE(i)
#             nodes.append(parent)
#         else:
#             child = NODE(i)
#             nodes.append(child)
#             nodes[company[i]].addChild(child)
#     nodes[0].DFS()
#     return nodes[0].time

# print(solution([-1, 0, 0, 1, 3]))



def solve(idx, nodes):
    rst = 1
    vec = []
    if len(nodes[idx]) > 0:
        mx = 0
        for i in range(len(nodes[idx])):
            vec.append(solve(nodes[idx][i], nodes))
            vec.sort(reverse=True)
        for i in range(len(vec)):
            mx = max(mx, vec[i]+i)
        rst += mx
    
    return rst


def solution(company):
    answer = 0
    nodes = [[] for i in range(len(company))]
    for i in range(1, len(company)):
        nodes[company[i]].append(i)
        
    print(nodes)
    
    answer = solve(0, nodes) -1
    return answer

print(solution([-1, 0, 0, 1, 3]))