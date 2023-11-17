text = '1'
while True:
    text = input()
    if text == '#':
        break
    count = sum(1 for char in text if char.lower() in ['a', 'e', 'i', 'o', 'u'])
    print(count)
