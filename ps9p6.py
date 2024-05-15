import re

pattern = re.compile(r'\b\w*z\w*\b', re.IGNORECASE)

teststrings = ["the quick brown fox jumps over the lazy dog.", "python exercises."]

for teststring in teststrings:
    if pattern.search(teststring):
        print(f'"{teststring}" contains a word with "z"')
    else:
        print(f'"{teststring}" does not contain a word with "z"')
