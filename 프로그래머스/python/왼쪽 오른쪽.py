def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        item = str_list[i]
        if item == 'l':
            answer = str_list[:i]
            break
        elif item == 'r':
            answer = str_list[i+1:]
            break
    return answer


print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
