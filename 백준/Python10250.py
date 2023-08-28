testCase = int(input())
answer = []

for i in range(testCase):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1

    if floor == 0:
        floor = H
        room -= 1

    roomNumber = floor * 100 + room
    answer.append(roomNumber)

print(*answer, sep="\n")

"""
문자열 연결:
python
Copy code
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2
print(result)  # 출력: Hello, World
문자열 포맷팅:
python
Copy code
name = "Alice"
age = 25
message = "My name is {}. I'm {} years old.".format(name, age)
print(message)  # 출력: My name is Alice. I'm 25 years old.

# 또는 f-strings를 사용할 수도 있습니다.
message = f"My name is {name}. I'm {age} years old."
print(message)  # 출력: My name is Alice. I'm 25 years old.
문자열 분할:
python
Copy code
sentence = "Hello, World!"
words = sentence.split(", ")
print(words)  # 출력: ['Hello', 'World!']
문자열 합치기:
python
Copy code
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # 출력: Hello World
문자열 변경:
python
Copy code
text = "Hello, World!"
new_text = text[:5] + "Python" + text[7:]
print(new_text)  # 출력: Hello Python!
"""
