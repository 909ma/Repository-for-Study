def solution(myString, pat):
    answer = ''
    size = len(pat)
    for i in range(len(myString) - size + 1):
        temp = myString[-i-size:][:size]
        if temp == pat:
            if i:
                answer = myString[:-i]
                break
            else:
                answer = myString
                break

    return answer


print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))


"""
solution=lambda x,y:x[:x.rindex(y)+len(y)]


rindex(), rfind()가 뭐지
"""
"""
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]


아하...
"""
