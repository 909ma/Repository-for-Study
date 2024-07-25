while True:
    line = input()
    if line == ".":
        break

    stack = []
    check = True

    for char in line:
        if char in "([":  # 여는 괄호일 때
            stack.append(char)
        elif char in ")]":  # 닫는 괄호일 때
            if not stack:  # 스택이 비어있으면 올바른 괄호가 아님
                check = False
                break
            top = stack.pop()
            if char == ")" and top != "(":
                check = False
                break
            elif char == "]" and top != "[":
                check = False
                break

    if check and not stack:  # 스택이 비어있어야 모든 괄호가 맞음
        print("yes")
    else:
        print("no")
