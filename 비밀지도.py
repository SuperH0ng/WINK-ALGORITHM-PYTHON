def solution(n, arr1, arr2):

    answer = []
    
    
    for _ in range(n):
        arr1[_] = bin(arr1[_])[2:].zfill(n)
        arr2[_] = bin(arr2[_])[2:].zfill(n)

        x=''


        for i in range(n):


            
            
            if arr1[_][i] == '1' or arr2[_][i] == '1':
                x += '#'
            else :
                x += ' '


        answer.append(x)

    
    
    return answer

