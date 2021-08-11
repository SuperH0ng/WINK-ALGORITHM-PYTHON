def solution(citations):

    citations.sort()

    answer = []
    
    for _ in citations :
        answer.append(min(_, len(citations)-(citations.index(_))))
        
    return max(answer)
