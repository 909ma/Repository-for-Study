def solution(k, score):
    answer = []
    output = []
    for _ in range(k):
        answer.append(-1)
        
    for item in score:
        if answer[0] < item:
            answer[0] = item
            answer.sort()
        
        for temp in answer:
            if temp == -1:
                pass
            else:
                output.append(temp)
                break
    return output


"""
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer


헐 왜 이런 생각을 못했지
"""
