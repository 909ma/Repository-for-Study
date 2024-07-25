def solution(arr, delete_list):
    answer = []
    for item in arr:
        if item in delete_list:
            pass
        else:
            answer.append(item)
    return answer


print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))


"""
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]

압축해서 적는게 좋은가?
not in은 배우자
"""
"""
def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

remove()도 있네
