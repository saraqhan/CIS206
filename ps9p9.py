import re

text = 'the quick brown fox jumps over the lazy dog.'
searchedword = 'fox'

match = re.search(searchedword, text)

if match:
    print(f'"{searchedword}" found in the text at index {match.start()}.')
else:
    print(f'"{searchedword}" not found in the text.')
