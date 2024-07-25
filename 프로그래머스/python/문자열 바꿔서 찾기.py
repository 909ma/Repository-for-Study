def solution(myString, pat):
    check = myString.replace("A", "Z").replace("B", "A").replace("Z", "B")
    if pat in check:
        answer = int(True)
    else:
        answer = int(False)
    return answer


print(solution("ABBAA", "AABB"))
print(solution("ABAB", "ABAB"))


"""
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))


pat을 건드려서 숏코딩 1등을 노리네. 이런 테크닉이?
"""
