def solution(a, b):
    answer = str(int(a)+int(b))
    return answer


print(solution("582", "734"))
print(solution("18446744073709551615", "287346502836570928366"))
print(solution("0", "0"))


"""
def solution(a, b):
    return str(eval(a+'+'+b))

    
eval()을 이렇게 써야 하구나
"""
