def solution(board, k):
    answer = 0
    i = len(board)
    j = len(board[0])

    for a in range(i):
        for b in range(j):
            if a + b <= k:
                answer += board[a][b]
    return answer


print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))