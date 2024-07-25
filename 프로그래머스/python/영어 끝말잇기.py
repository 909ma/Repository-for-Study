def solution(n, words):
    temp = words[0][0]
    player = 0
    word_num = 1
    word_list = []
    for item in words:
        if player >= n:
            player = 1
            word_num += 1
        else:
            player += 1
        if item[0] == temp:
            if item in word_list:
                return [player, word_num]
            else:
                word_list.append(item)
                temp = item[-1]
        else:
            return [player, word_num]
    return [0, 0]


# Test Cases
print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


"""
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
        
        
변수 선언 하지 말껄
이전의 값이 필요하면 item 하지 말자
"""
