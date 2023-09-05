def solution(myString):
    split_list = myString.split("x")
    split_list = [item.strip() for item in split_list if item.strip() != ""]
    answer = sorted(split_list)
    return answer


"""
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)
    
    
잘 줄였네
"""
"""
def solution(myString):
    answer = ' '.join(myString.split('x')).split()
    return sorted(answer)


신기하군
"""
