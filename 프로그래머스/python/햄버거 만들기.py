def solution(ingredient):
    s = ''.join(map(str, ingredient))
    
    stack = []
    pattern = ['1', '2', '3', '1']
    answer = 0
    
    for ch in s:
        stack.append(ch)
        if stack[-4:] == pattern:
            del stack[-4:]
            answer += 1
    
    return answer

def main():
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # 2
    print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # 0

if __name__ == "__main__":
    main()


"""
def check_list(target_list:list):
    is_need_check = False
    for index in range(len(target_list) - 3):
        if target_list[index:index+4] == [1, 2, 3, 1]:
            del target_list[index:index+4]
            is_need_check = True
            return is_need_check, target_list
    return is_need_check, None

def solution(ingredient):
    answer = -1
    is_need_check = True

    while is_need_check:
        answer += 1
        is_need_check, ingredient = check_list(ingredient)
                                    
    return answer


def main():
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
    print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))

if __name__ == "__main__":
    main()


처음엔 이렇게 풀었더니 시간 초과가 떴다.
"""

"""
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt


다른 사람은 큐로 풀었더라
"""




