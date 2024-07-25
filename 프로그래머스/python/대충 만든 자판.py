def search_char(string, target_char):
    for index, item in enumerate(string):
        if item == target_char:
            return index + 1
        
    return 0

def solution(keymap, targets):
    answer = []
    
    for item in targets:
        add_index = 0
        
        for target_char in item:
            index = 101
            
            for check_list in keymap:
                temp_index = search_char(check_list, target_char)
                if temp_index != 0:
                    index = min(index, temp_index)

            add_index += index
            if index == 101:
                add_index = -1
                break
                
        answer.append(add_index)
    return answer
