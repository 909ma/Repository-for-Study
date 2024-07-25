def solution(arr, queries):
    for query in queries:
        i, j = query
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr


"""
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr


...
"""
