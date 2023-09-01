def solution(num_list):
    num1 = num_list[-1]
    num2 = num_list[-2]
    if num1 > num2:
        num_list.append(num1 - num2)
    else:
        num_list.append(num1 * 2)
    return num_list

print(solution([2, 1, 6]))
print(solution([5, 2, 1, 7, 5]))
