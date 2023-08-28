string = input()

result = ""
for char in string:
    if char.islower():
        result += char.upper()
    else:
        result += char.lower()

print(result)
