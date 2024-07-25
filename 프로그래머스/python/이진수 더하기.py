def solution(bin1, bin2):
    answer = ''
    carry = 0
    if bin1 == "0":
        return bin2
    elif bin2 == "0":
        return bin1
    elif len(bin1) > len(bin2):
        bin2 = "0" * (len(bin1) - len(bin2)) + bin2
    elif len(bin1) < len(bin2):
        bin1 = "0" * (len(bin2) - len(bin1)) + bin1

    for i in range(1, len(bin1) + 1):
        add_list = sum([int(bin1[-i]), int(bin2[-i]), carry])
        # print(f"{add_list} {bin1} {bin2} {answer}")
        if add_list == 0:
            answer += "0"
            carry = 0
        elif add_list == 1:
            answer += "1"
            carry = 0
        elif add_list == 2:
            answer += "0"
            carry = 1
        elif add_list == 3:
            answer += "1"
            carry = 1
    if carry == 1:
        answer += "1"
    return answer[::-1]


# Test Cases
print(solution("10", "11"))
print(solution("1001", "1111"))
print(solution("1001", "11"))
print(solution("1001", "0"))


"""
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
    
    
헐ㅋ
"""
"""
def solution(bin1, bin2):
    answer = 0
    bin1_size = len(bin1)
    bin2_size = len(bin2)

    sum = 0

    for i in bin1:
        sum += int(i) * (2 ** (bin1_size - 1))
        bin1_size -= 1

    for i in bin2:
        sum += int(i) * (2 ** (bin2_size - 1))
        bin2_size -= 1

    answer = str(bin(sum))[2:]



    return answer
    

좋네 나중에 다시 풀자
"""
