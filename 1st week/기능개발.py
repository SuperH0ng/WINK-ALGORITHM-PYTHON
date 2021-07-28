def solution(progresses, speeds):
    from math import ceil
    times = []
    for _ in range(len(progresses)) :
        times.append(ceil((100-progresses[_])/(speeds[_])))

    answer = []
    pri = 0
    cnt = 1

    for i in range(0,(len(times)-1)):
        if times[pri] >= times[i+1]:
            cnt += 1
        else :
            answer.append(cnt)
            pri = i+1
            cnt = 1
            
    answer.append(cnt)
    return answer
