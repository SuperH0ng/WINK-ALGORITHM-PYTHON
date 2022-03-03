def solution(input_string):
    answer = ''
    check = list([0, True] for i in range(26))
    sList = list(input_string) + ['A']
    
    for i in range(len(sList) - 1) :
        alphaNum = ord(sList[i]) - 97
        check[alphaNum][0] += 1  
        if sList[i] == sList[i+1] :
            check[alphaNum][1] = False
    
    for j in range(26) :
        if check[j][0] > 1 and check[j][1] == True :
            answer += chr(j + 97)
    
    print(sList)
    print(check)
    if answer == '' :
        return 'N'
    return answer

print(solution("edeaaabbccd"))
print(solution("string"))
