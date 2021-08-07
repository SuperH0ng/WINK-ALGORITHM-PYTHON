def solution(priorities, location):
    x = [priorities[location],location]
    tag = []
    for _ in range(len(priorities)) :
        tag.append([priorities[_], _])


    
    for i in range(len(priorities)-1):
        while priorities[i] < max(priorities[i+1:]):
            tag.append(tag.pop(i))
            priorities.append(priorities.pop(i))


    
    answer = tag.index(x)+1


    
    return answer
