def solution(age):
    age_str = str(age)
    char_map = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j'
    }
    answer = ''.join(char_map[char] for char in age_str)
    return answer


# Test Cases
print(solution(23))
print(solution(51))
print(solution(100))


"""
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])
    

이걸 까먹었네
"""
