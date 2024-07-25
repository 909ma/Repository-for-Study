from collections import deque

n, k = map(int, input().split())  # 사람 수 n, 제거할 순서 k

people = deque(range(1, n + 1))  # 1부터 n까지의 숫자로 큐 초기화
result = []

while people:
    people.rotate(-k + 1)  # 큐를 k - 1번 왼쪽으로 회전
    result.append(str(people.popleft()))  # 제거할 사람을 결과 리스트에 추가

answer = ", ".join(result)  # 결과 리스트를 문자열로 변환하여 출력 형식에 맞춤

print(f"<{answer}>")
