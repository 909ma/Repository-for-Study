def solution(n, k):
    answer = []
    temp = k
    while temp <= n:
        answer.append(temp)
        temp += k
    return answer


print(solution(10, 3))
print(solution(15, 5))


"""
def solution(n, k):
    return [i for i in range(k,n+1,k)]
    

괜찮네;
"""
