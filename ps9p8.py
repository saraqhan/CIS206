text = 'The quick brown fox jumps over the lazy dog.'
searchedwords = ['fox', 'dog', 'horse']

for word in searchedwords:
    if word in text:
        print(f'"{word}" found in the text.')
    else:
        print(f'"{word}" not found in the text.')
