def solution(s):
    if s.count("p") + s.count("P") == s.count("y") + s.count("Y"):
        return True
    else:
        return False


# Test Cases
print(solution("pPoooyY"))
print(solution("pPoooyY"))


"""
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )



헐
"""
