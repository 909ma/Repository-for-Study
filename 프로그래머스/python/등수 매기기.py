def solution(score):
    answer = []
    avg_score = []
    [avg_score.append(sum(item)/2) for item in score]
    rank = sorted(avg_score, reverse=True)
    [answer.append(rank.index(item) + 1) for item in avg_score]
    return answer


# Test Cases
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print("="*50)
print(solution([[80, 70], [70, 80], [30, 50], [
      90, 100], [100, 90], [100, 100], [10, 30]]))
print("="*50)


"""
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
    
    
아 이렇게 할 껄
"""
