def solution(id_pw, db):
    for item in db:
        if item[0] == id_pw[0]:
            if item[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"


# Test Cases
print(solution(["meosseugi", "1234"], [["rardss", "123"],
      ["yyoom", "1234"], ["meosseugi", "1234"]]))
print("="*50)
print(solution(["programmer01", "15789"], [["programmer02", "111111"], [
      "programmer00", "134"], ["programmer01", "1145"]]))
print("="*50)
print(solution(["rabbit04", "98761"], [["jaja11", "98761"],
      ["krong0313", "29440"], ["rabbit00", "111333"]]))
print("="*50)


"""
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"


신기하네
"""
