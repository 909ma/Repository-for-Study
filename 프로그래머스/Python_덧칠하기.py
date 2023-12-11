def solution(n, m, section):
    answer = 0
    wall_list = []
    for _ in range(n + 1):
        wall_list.append(True)
    for item in section:
        wall_list[item] = False

    print(wall_list)
        
    for i in range(1, n + 1):
        print(i, "before", wall_list)
        if wall_list[i] == False:
            for j in range(i, min(i + m, n + 1)):
                wall_list[j] = True
            answer += 1
            print("check")
        print(i, "after", wall_list)

    return answer



print(solution(8, 4, [2, 3, 6]))


"""
야근을 너무 늦게까지했다...
정말 피곤하다....
"""

