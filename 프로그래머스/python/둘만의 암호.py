def solution(s, skip, index):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    secret_alphabet = []
    skip_alphabet = []
    
    for item in skip:
        skip_alphabet.append(item)
        
    for item in alphabet:
        if item not in skip_alphabet:
            secret_alphabet.append(item)
    
    answer = ''
    for item in s:
        answer += secret_alphabet[(secret_alphabet.index(item) + index) % len(secret_alphabet)]
    
    return answer
