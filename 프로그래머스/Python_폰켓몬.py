def solution(nums):
    size_list = len(nums)
    size_set = len(set(nums))
    return size_set if size_list // 2 >= size_set else size_list // 2

"""
def solution(ls):
    return min(len(ls)/2, len(set(ls)))


min()을 까먹었네잉
"""
