def solution(array, commands):

    answer = []

    for _ in range(len(commands)) :
        
        newArray = sorted(array[((commands[_][0])-1):(commands[_][1])])
        
        answer.append(newArray[(commands[_][2]-1)])
    
    return answer
