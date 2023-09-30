def solution(polynomial):
    answer = ''
    temp = polynomial.split(" + ")
    num1 = 0
    num2 = 0

    for item in temp:
        if "x" in item:
            if item == "x":
                num1 += 1
            else:
                num1 += int(item.replace("x", ""))
        else:
            num2 += int(item)

    if num1 == 0:
        return str(num2)
    elif num1 == 1:
        if num2 != 0:
            return f"x + {num2}"
        else:
            return "x"
    else:
        if num2 != 0:
            return f"{num1}x + {num2}"
        else:
            return f"{num1}x"

    return answer


# Test Cases
print(solution("3x + 7 + x"))
print("="*50)
print(solution("x + x + x"))
print("="*50)
