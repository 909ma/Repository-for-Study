N, M = map(int, input().split())

while N != 0 and M != 0:
    cd_set = set()
    answer = 0

    for _ in range(N):
        cd = int(input())
        cd_set.add(cd)

    for _ in range(M):
        cd = int(input())
        if cd in cd_set:
            answer += 1

    print(answer)

    N, M = map(int, input().split())
