def solution(bridge_length, weight, truck_weights):


    answer = [0] * bridge_length
    time = 0

    while len(truck_weights) > 0:
        time += 1
        answer.pop(0)
        if sum(answer) + truck_weights[0] <= weight :
            answer.append(truck_weights.pop(0))
        else :
            answer.append(0)

        print(truck_weights)
        
    
        
        
    time = time + bridge_length

    return time
