def solution(emergency):
    answer = []
    sorted_list = sorted(emergency, reverse=True)
    for item in emergency:
        for i in range(len(sorted_list)):
            if item == sorted_list[i]:
                answer.append(i+1)
                break
    return answer


# Test Cases
print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))


"""
def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]
    

index(ㅑ) 같은 것도 있네...
"""
