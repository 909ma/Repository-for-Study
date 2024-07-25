def solution(myString, pat):
    answer = int(False)
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        answer = int(True)
    return answer


print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))
