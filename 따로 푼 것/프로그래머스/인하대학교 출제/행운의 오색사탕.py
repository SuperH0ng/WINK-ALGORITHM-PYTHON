def solution(candy, positions):
    answer = []
    for p in positions :
        if p <= 1 :
            answer += [0]
            continue
        answer += [colorfulCandy(candy[:p])]
        # print("하나 끝")
    return answer

def colorfulCandy(candy) :
    answer = 0
    front = candy[0]
    frontP = candy[0]
    end = candy[-1]
    endP = candy[-1]
    i = 1
    while (i < len(candy)) :
        
        
        
        if front == end :
            # print(i)
            # print(front)
            # print(end)
            # print("같")
            answer += 1
            front += candy[i]
            end = candy[-i-1] + end
            i += 1
            
        elif front[1:] == end[:-1] :
            # print(i)
            # print(front)
            # print(end)
            # print("-1까지 같")
            front += candy[i]
            end = candy[-i-1] + end
            i += 1
        else :
            # print(i)
            l = len(front)
            # print(front)
            # print(end)
            # print("안 같")
            front += candy[i:i + l]
            end = candy[-i -l : -i ] + end
            i += l

    return answer

print(solution("RYRYRGPRYRYRBB", [12, 1, 14]))
print(solution("BPBRBPBRB", [3, 6, 9]))
print(solution("ABCAEFBCABABCAEFBCAB", [4, 10, 20]))





def solution(candy, positions):
    answer = []
    for p in positions:
        answer.append(0)
        b_candy = candy[0:p]
        for i in range(1, len(b_candy)-1):
            if b_candy[0] == b_candy[-i]:
                front = b_candy[0:i]
                back = b_candy[-i:len(b_candy)]
                if front == back:
                    answer[-1] += 1
    return answer