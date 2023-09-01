from collections import deque


def solution(n, control):
    control = deque(control)
    while len(control):
        char = control.pop()
        if char == "w":
            n += 1
        elif char == "s":
            n -= 1
        elif char == "d":
            n += 10
        else:
            n -= 10
    return n

print(solution(0, "wsdawsdassw"))

"""
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

잘했네...
"""
