def solution(numbers):
    answer = numbers.replace("zero", "0")
    answer = answer.replace("one", "1")
    answer = answer.replace("two", "2")
    answer = answer.replace("three", "3")
    answer = answer.replace("four", "4")
    answer = answer.replace("five", "5")
    answer = answer.replace("six", "6")
    answer = answer.replace("seven", "7")
    answer = answer.replace("eight", "8")
    answer = answer.replace("nine", "9")
    return int(answer)


# Test Cases
print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))


"""
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
    
    
이런 방법이?
"""
"""
def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)
    

딕셔너리 괜찮네
"""
