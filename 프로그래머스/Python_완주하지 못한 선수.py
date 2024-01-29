def solution(participant, completion):
    list1 = sorted(participant)
    list2 = sorted(completion)
    
    for i, item in enumerate(list1):
        if i < len(list2) and list1[i] != list2[i]:
            return item
        elif i == len(list2):
            return item
        
    return -1

"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


내 코드보다 낫다
"""
"""
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


해시 풀이
"""
"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


이런게 있네
"""
