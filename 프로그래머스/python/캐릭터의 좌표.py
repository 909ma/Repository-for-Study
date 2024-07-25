def solution(keyinput, board):
    answer = [0, 0]
    margin_x = (board[0] - 1) // 2
    margin_y = (board[1] - 1) // 2
    for key in keyinput:
        if key == "up":
            if answer[1] == margin_y:
                pass
            else:
                answer[1] += 1
        elif key == "down":
            if answer[1] == -margin_y:
                pass
            else:
                answer[1] -= 1
        elif key == "left":
            if answer[0] == -margin_x:
                pass
            else:
                answer[0] -= 1
        elif key == "right":
            if answer[0] == margin_x:
                pass
            else:
                answer[0] += 1
    return answer


# Test Cases
print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print("="*50)
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
print("="*50)


"""
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]
    
    
내 코드 개선점이 여기에 있네
"""
"""
def solution(keyinput, board):
    curr = [0, 0]
    for k in keyinput:
        if k == 'left':
            curr[0] = max(curr[0] - 1, -(board[0] // 2))
        elif k == 'right':
            curr[0] = min(curr[0] + 1, board[0] // 2)
        elif k == 'down':
            curr[1] = max(curr[1] - 1, -(board[1] // 2))
        else:
            curr[1] = min(curr[1] + 1, board[1] // 2)

    return curr


신기하네 대박
"""
