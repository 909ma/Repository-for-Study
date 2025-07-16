def solution(board, moves):
    answer = 0
    row = len(board)
    output_list = []
    for index in moves:
        is_check = True
        for i in range(row):
            target = board[i][index - 1]
            # print(f"-->{target}")
            if target == 0:
                continue
            else:
                while len(output_list) > 0:
                    pre_target = output_list.pop()
                    if pre_target == target:
                        is_check = False
                        answer += 1
                        # print("++answer")
                        continue
                    else:
                        output_list.append(pre_target)
                        break
                        
                if is_check:
                    output_list.append(target)
                else:
                    answer += 1
                board[i][index - 1] = 0
                break
        # print(output_list)
        
    return answer


input_board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
input_moves = [1,5,3,5,1,2,1,4]
output = solution(
    board=input_board,
    moves=input_moves
)
print(output)


"""
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""
