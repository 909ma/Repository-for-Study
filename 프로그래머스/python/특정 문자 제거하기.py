def solution(my_string, letter):
    return my_string.replace(letter, "")


# Test Cases
print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
