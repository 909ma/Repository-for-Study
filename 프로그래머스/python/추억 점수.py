def solution(name, yearning, photo):
    answer = []
    
    for check_list in photo:
        temp_sum = 0
        for target, score in zip(name, yearning):
            if target in check_list:
                temp_sum += score
        answer.append(temp_sum)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))


"""
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]

잘 줄여쓰네
"""
