def solution(cards1, cards2, goal):
    answer = ''
    i, j = 0, 0
    for item in goal:
        if item == cards1[i]:
            if i != len(cards1) - 1:
                i += 1
        elif item == cards2[j]:
            if j != len(cards2) - 1:
                j += 1
        else:
            return "No"
    return "Yes"


"""
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
    

Queue로 풀까 고민했는데... 아깝네
"""
