def solution(s1, s2):
    answer = 0
    for item1 in s1:
        for item2 in s2:
            if item1 == item2:
                answer += 1
    return answer


# Test Cases
print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))


"""
def solution(s1, s2):
    return len(set(s1)&set(s2))
    
    
아 비트연산자를 이렇게 쓰면 되구나
"""
