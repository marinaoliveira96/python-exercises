def contains_substring(sentence: str) -> bool:
    return 'python' in sentence.lower()


sentences = ['I am learning Python', 'I am learning python', 'Hello Word']

for sentence in sentences:
    if contains_substring(sentence):
        print(f'Found in "{sentence}"')
    else:
        print(f'Not found in "{sentence}"')
        
# Found in "I am learning Python"
# Found in "I am learning python"
# Not found in "Hello Word"'