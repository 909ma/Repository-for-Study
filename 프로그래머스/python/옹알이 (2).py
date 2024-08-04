def solution(babbling):
    result = 0
    for target in babbling:
        i = -1
        while True:
            if target.startswith("aya"):
                if i == 1:
                    break
                i = 1
                if len(target) == 3:
                    result += 1
                    break
                else:
                    target = target[3:]
            elif target.startswith("ye"):
                if i == 2:
                    break
                i = 2
                if len(target) == 2:
                    result += 1
                    break
                else:
                    target = target[2:]
            elif target.startswith("woo"):
                if i == 3:
                    break
                i = 3
                if len(target) == 3:
                    result += 1
                    break
                else:
                    target = target[3:]
            elif target.startswith("ma"):
                if i == 4:
                    break
                i = 4
                if len(target) == 2:
                    result += 1
                    break
                else:
                    target = target[2:]
            else:
                break
    return result

