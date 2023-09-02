def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        found = False
        min_greater = float('inf')
        
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < min_greater:
                min_greater = arr[i]
                found = True
        
        if found:
            answer.append(min_greater)
        else:
            answer.append(-1)
    
    return answer
