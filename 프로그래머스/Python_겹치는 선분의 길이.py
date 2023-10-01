def solution(lines):
    temp = []
    temp2 = []
    for item in lines:
        for i in range(item[0], item[1]):
            if i + 0.5 in temp:
                if i + 0.5 not in temp2:
                    temp2.append(i + 0.5)
            else:
                temp.append(i + 0.5)
    return len(temp2)


# Test Cases
print(solution([[0, 1], [2, 5], [3, 9]]))
print("=" * 50)
print(solution([[-1, 1], [1, 3], [3, 9]]))
print("=" * 50)
print(solution([[0, 5], [3, 9], [1, 10]]))
print("=" * 50)


"""
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    
    
헐ㅋ
"""
"""
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

        
더 직관적이네
"""
