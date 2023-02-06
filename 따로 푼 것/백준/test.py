graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B', 'G'],
    'E' : ['B', 'H', 'I'],
    'F' : ['C', 'J'],
    'G' : ['D'],
    'H' : ['E'],
    'I' : ['E'],
    'J' : ['F']
}

check = {
    'A' : False,
    'B' : False,
    'C' : False,
    'D' : False,
    'E' : False,
    'F' : False,
    'G' : False,
    'H' : False,
    'I' : False,
    'J' : False
}

def dfs(node) :
    check[node] = True
    

    for n in graph[node] :
        
        if not check[n] :
            dfs(n)
            
    # 어떤 특정한 동작을 하는 코드
    print(node, end=' ')


            
dfs('A')