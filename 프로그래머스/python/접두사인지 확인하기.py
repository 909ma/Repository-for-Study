def solution(my_string, is_prefix):
    size = len(is_prefix)
    if len(my_string) < size:
        answer = int(False)
    else:
        answer = int(my_string[:size] == is_prefix)
    return answer


print(solution("banana", "ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))


"""
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

날먹 당했다
"""
