def solution(my_string):
    for item in ["a", "e", "i", "o", "u"]:
        my_string = my_string.replace(item, "")
    return my_string


# Test Cases
print(solution("bus"))
print(solution("nice to meet you"))


"""
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
    
    
join() 연습할껄
"""
