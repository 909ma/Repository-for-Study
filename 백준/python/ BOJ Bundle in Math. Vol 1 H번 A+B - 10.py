for a in range(1, 10):
    print("? A", a, flush=True)
    resp = int(input())
    if resp == 1:
        for b in range(1, 10):
            print("? B", b, flush=True)
            resp = int(input())
            if resp == 1:
                print("!", a + b)
                break
                break

"""
인터랙티브는 처음인데 생소하고 신기하네 ㅋㅋㅋ
"""
