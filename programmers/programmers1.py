from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    answer = 0
    total_weight = 0
    
    while(bridge):
        answer += 1
        total_weight -= bridge.popleft()
        if(truck_weights):
            if (truck_weights[0] + total_weight <= weight):
                total_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
