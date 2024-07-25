def solution(spell, dic):
    spell.sort()
    check_voca = "".join(spell)
    for item in dic:
        item = "".join(sorted(list(item)))
        if item == check_voca:
            return 1
    return 2


# Test Cases
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print("="*50)
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print("="*50)
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))


"""
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
    
    
왜 집합을 생각하지 못했을까
"""
