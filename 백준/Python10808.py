array1 = [0] * 26
inputLine = input()
length = len(inputLine)
for i in range(length - 1, -1, -1):
    num = ord(inputLine[i]) - ord('a')
    array1[num] += 1

print(*array1, sep=' ')

"""
아스타리스크는 왜 붙은거야?

ChatGPT
코드에서 print(*array1, sep=' ')와 같이 앞에 *을 붙인 것은, 리스트 array1의 각 요소를 개별적인 인자로 전달하는 것을 의미합니다. 이를 언패킹(unpacking)이라고 합니다.

print() 함수는 기본적으로 여러 개의 인자를 받을 수 있습니다. 리스트는 하나의 인자로 전달되지만, *을 사용하여 리스트의 각 요소를 개별적인 인자로 분리하여 print() 함수에 전달하면, 리스트의 각 요소가 개별적으로 출력됩니다.

따라서, print(*array1, sep=' ')는 print(array1[0], array1[1], array1[2], ..., sep=' ')와 같은 효과를 가지며, 리스트의 각 요소가 공백으로 구분되어 출력됩니다.

앞의 예시에서 *array1를 사용하여 리스트의 각 요소를 언패킹하고, sep=' '를 사용하여 요소 사이에 공백을 설정한 결과로 인해 공백으로 구분된 출력이 가능해집니다.
"""
