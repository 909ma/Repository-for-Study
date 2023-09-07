def solution(myStr):
    answer = []
    temp = ""
    for i in range(len(myStr)):
        if myStr[i] in "abc":
            if temp == "":
                pass
            else:
                answer.append(temp)
                temp = ""
        else:
            temp += myStr[i]
    if myStr[-1] not in "abc":
        answer.append(temp)
    if not (len(answer)):
        answer.append("EMPTY")
    return answer


print(solution("baconlettucetomato"))
print(solution("abcd"))
print(solution("cabab"))

"""
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']


센스있네;;;
"""
"""
def solution(myStr):
    s=myStr.replace('b','a')
    s=s.replace('c','a')
    s=s.split('a')
    answer=[]
    for x in s:
        if x: answer.append(x)
    if not answer:return ["EMPTY"]
    return answer
    
    
나도 다음에는 이런 생각해야겠다
"""
"""
import re
def solution(myStr):
    answer = [m for m in re.split('a|b|c',myStr) if m]
    if len(answer)==0:
        answer=["EMPTY"]

    return answer
    
    
신기하네. re 라이브러리가 뭐지?
"""
