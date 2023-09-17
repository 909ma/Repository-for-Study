from collections import defaultdict

# 입력 처리
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 각 숫자의 출현 횟수를 저장할 딕셔너리 생성
card_count = defaultdict(int)

# 카드의 출현 횟수를 계산하여 딕셔너리에 저장
for card in cards:
    card_count[card] += 1

# 대상 숫자에 대한 결과 출력
for target in targets:
    print(card_count[target], end=' ')
