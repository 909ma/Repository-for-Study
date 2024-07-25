def solution(order):
    answer = 0
    for item in order:
        if 'cafelatte' in item:
            answer += 5000
        else:
            answer += 4500
    return answer


print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
print(solution(["americanoice", "americano", "iceamericano"]))
