def solution(n):
    x, y = 0, 0
    for a, b in n:
        x = max(x, max(a, b))
        y = max(y, min(a, b))
    return x*y


# Test Cases
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


"""
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)


와
"""
