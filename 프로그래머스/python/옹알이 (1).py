def solution(babbling):
    answer = 0
    for item in babbling:
        item = item.replace("aya", "1")
        item = item.replace("ye", "2")
        item = item.replace("woo", "3")
        item = item.replace("ma", "4")

        item = item.replace("1", "")
        item = item.replace("2", "")
        item = item.replace("3", "")
        item = item.replace("4", "")
        if len(item) == 0:
            answer += 1
    return answer


# Test Cases
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print("=" * 50)
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
print("=" * 50)


"""
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt
    
    
이게 머임
"""
