def solution(N, stages):
    answer = []
    count_list1 = []
    count_list2 = []
    people = len(stages)
    for i in range(1, N + 1):
        if people == 0:
            count_list1.append(0)
            count_list2.append(0)
        else:
            count_list1.append((stages.count(i)/people))
            count_list2.append((stages.count(i)/people))
            people -= stages.count(i)
    count_list2.sort()

    # print(count_list1)
    # print(count_list2)
    for _ in range(N):
        search_target = count_list2.pop()
        for i in range(N):
            if search_target == count_list1[i]:
                if i + 1 not in answer:
                    answer.append(i + 1)
    # print("=" * 10)
    return answer


print(solution(7, [2, 1, 2, 6, 2, 4, 3, 3]))


"""
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


딕셔너리가 편하긴 하지
"""
