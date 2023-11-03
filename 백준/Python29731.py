promise = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you',
           'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']
test_cases = int(input())
check = True
for _ in range(test_cases):
    text = input()
    if text not in promise:
        check = False

print("No") if check else print("Yes")
