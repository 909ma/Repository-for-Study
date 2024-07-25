def solution(myString, pat):
    answer = 0
    pat_length = len(pat)
    for i in range(len(myString)):
        if i + pat_length > len(myString):
            break
        else:
            if myString[i:i+pat_length] == pat:
                answer += 1
    return answer


"""
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
    
    
나도 .startswith(), enumerate() 잘 써야겠다
"""
