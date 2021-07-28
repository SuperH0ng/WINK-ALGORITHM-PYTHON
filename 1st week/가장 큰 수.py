def solution(numbers):
    answer = ''
    
    numbers = list(map(str,numbers))
    for i in range(len(numbers)) :
        numbers[i] = (numbers[i])*3
        
    numbers = sorted(numbers, reverse=True)

    for l in range(len(numbers)) :
        if len(numbers[l]) == 12 :
            numbers[l] = int(numbers[l])//100010001
        elif len(numbers[l]) == 9 :
            numbers[l] = int(numbers[l])//1001001
        elif len(numbers[l]) == 6 :
            numbers[l] = int(numbers[l])//10101
        elif len(numbers[l]) == 3 and numbers[l] != '000':
            numbers[l] = int(numbers[l])//111
        elif numbers[l] == '000':
            numbers[l] = 0


    for _ in range(len(numbers)) :
        answer += str(numbers[_])

    answer = str(int(answer))
        
    return answer
