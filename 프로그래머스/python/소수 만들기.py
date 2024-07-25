import math

def solution(nums):
    answer = math.comb(len(nums), 3)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums), 1):
            for k in range(j + 1, len(nums), 1):
                temp = nums[i] + nums[j] + nums[k]
                for l in range(2, (temp + 1) // 2, 1):
                    if temp % l == 0:
                        answer -= 1
                        break
    return answer


"""
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer


이렇게도 쓸 수 있네
for if else 구문 처음 알았다
"""
