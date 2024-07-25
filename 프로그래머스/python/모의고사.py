def solution(answers):
    answer = []
    
    one_score = 0
    two_score = 0
    three_score = 0
    
    one_list = [1, 2, 3, 4, 5]
    two_list = [2, 1, 2, 3, 2, 4, 2, 5]
    three_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    while len(answers) != 0:
        temp_num = answers.pop(0)
        temp_one = one_list.pop(0)
        temp_two = two_list.pop(0)
        temp_three = three_list.pop(0)
        if temp_num == temp_one:
            one_score += 1
        if temp_num == temp_two:
            two_score += 1
        if temp_num == temp_three:
            three_score += 1
        one_list.append(temp_one)
        two_list.append(temp_two)
        three_list.append(temp_three)
        
    if max(one_score, two_score, three_score) == one_score:
        answer.append(1)
    if max(one_score, two_score, three_score) == two_score:
        answer.append(2)
    if max(one_score, two_score, three_score) == three_score:
        answer.append(3)
    return answer


"""
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


헐ㅋ
"""
