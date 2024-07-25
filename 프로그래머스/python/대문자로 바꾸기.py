def solution(myString):
    answer = myString.upper()
    return answer


print(solution("aBcDeFg"))
print(solution("AAA"))


"""
def solution(myString):
    answer = ''
    for i in myString:
        if i.islower:
            answer += i.upper()
        else:
            answer += i


    return answer

.islower 같은 것도 있네 
"""
