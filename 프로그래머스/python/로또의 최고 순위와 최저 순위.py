def solution(lottos, win_nums):
    answer = []
    temp_set = set(lottos)
    win_count = 0
    lose_count = 0
    for item in temp_set:
        if item != 0:
            if item in win_nums:
                win_count += 1
            else:
                lose_count += 1
    answer = [min(1 + lose_count, 6), min(7 - win_count, 6)]
    return answer

"""
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


앗
"""
