def solution(rsp):
    rsp = rsp.replace("2", "영")
    rsp = rsp.replace("0", "오")
    rsp = rsp.replace("5", "이")
    rsp = rsp.replace("영", "0")
    rsp = rsp.replace("오", "5")
    rsp = rsp.replace("이", "2")
    return rsp


# Test Cases
print(solution("2"))
print(solution("205"))


"""
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
    
    
아까 join 하기로 해놓고 이걸 또 까먹어?
"""
"""
def solution(rsp):
    return rsp.translate(str.maketrans('025', '502'))
    

이런 것도 있네
"""
