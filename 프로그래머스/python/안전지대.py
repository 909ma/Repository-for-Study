def solution(board):
    answer = 0
    n, m = len(board), len(board[0])

    check_list = [[0] * (m + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(m):
            check_list[i + 1][j + 1] = board[i][j]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp = (
                check_list[i][j] + check_list[i - 1][j - 1]
                + check_list[i][j - 1] + check_list[i + 1][j - 1]
                + check_list[i - 1][j] + check_list[i + 1][j]
                + check_list[i - 1][j + 1] + check_list[i][j + 1]
                + check_list[i + 1][j + 1]
            )
            if temp == 0:
                answer += 1
    return answer


# Test Cases
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print("=" * 50)
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print("=" * 50)
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
print("=" * 50)


"""
def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer
    
    
max, min을 써서 변두리 살아남는거 이걸 또 잊었네
"""
"""
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
    
    
이게 머임
"""
