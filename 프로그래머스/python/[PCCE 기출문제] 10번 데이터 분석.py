def solution(data, ext, val_ext, sort_by):
    answer = []
    
    type_list = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    sort_idx = type_list[sort_by]
    data.sort(key=lambda x: x[sort_idx])
    
    filter_idx = type_list[ext]
    for target in data:
        if target[filter_idx] < val_ext:
            answer.append(target)
            
    return answer

"""
def solution(data, ext, val_ext, sort_by):
    answer = []
    by = [ "code", "date", "maximum", "remain" ]

    for item in data:
        if item[by.index(ext)] < val_ext:
            answer.append(item)

    return sorted(answer, key=lambda x: x[by.index(sort_by)])
"""
