def solution(str_list, ex):
    temp = []
    for item in str_list:
        if ex in item:
            pass
        else:
            temp.append(item)
    answer = ''.join(temp)
    return answer


print(solution(["abc", "def", "ghi"], "ef"))
print(solution(["abc", "bbc", "cbc"], "c"))


"""
def solution(str_list, ex):
    filtered_list = [s for s in str_list if ex not in s]
    return "".join(filtered_list)


내 코드를 한 줄로 잘 줄였네
"""
"""
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))


filter()이 머지
filter(조건 함수, 순회 가능한 데이터)
신기하네
https://www.daleseo.com/python-filter/
"""
