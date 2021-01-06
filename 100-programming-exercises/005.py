def is_palindrom(word: str) -> bool:
    if word[::-1] == word:
        return True
    else:
        return False


words = ['kajak', 'inni', 'ananas', 'radar']
for word in words:
    if is_palindrom(word):
        print(f'{word} is a palindrom')
    else:
        print(f'{word} is not a palindrom')
        
# kajak is a palindrom
# inni is a palindrom
# ananas is not a palindrom
# radar is a palindrom

# [::-1] -1 esta indo de tras pra frente [begin:end:step]