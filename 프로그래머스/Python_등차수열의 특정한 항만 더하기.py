def solution(a, d, included):
    answer = 0
    a -= d
    for item in included:
        a += d
        if item:
            answer +=  a
    return answer


print(solution(3, 4, [True, False, False, True, True]))
print(solution(7, 1, [False, False, False, True, False, False, False]))

'''
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer
    
연산 속도가 내 꺼보다는 뒤지기는 할텐데 깔끔하네
'''

'''
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)

이게 가장 나은 듯?
'''
