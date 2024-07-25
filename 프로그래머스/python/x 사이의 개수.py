def solution(myString):
    temp = myString.split("x")
    answer = []
    for item in temp:
        answer.append(len(item))
    return answer


print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))
