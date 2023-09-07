def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        temp = 0
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        else:
            temp = answer.pop()
            if temp == arr[i]:
                i += 1
            else:
                answer.append(temp)
                answer.append(arr[i])
                i += 1

    if len(answer) == 0:
        answer.append(-1)
    return answer


print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))


"""
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]
    

9번째 줄에서 return stk or [-1] 는 어떻게 작동하나요? stk가 원소가 있으면, 즉 True이면 stk를 return하고. 그게 아니라면 (빈리스트=False라면) [-1]를 return 하나요?

객체1 or 객체2 연산은 bool(객체1)이 True이면 객체1을, False이면(비어 있으면) 객체2를 반환한다고 하네요!


아하
"""
