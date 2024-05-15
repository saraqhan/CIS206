import re

pattern = re.compile(r'^\w+')

teststrings = ["the quick brown fox jumps over the lazy dog.", " the quick brown fox jumps over the lazy dog."]

for teststring in teststrings:
    if pattern.match(teststring):
        print(f'"{teststring}" starts with a word')
    else:
        print(f'"{teststring}" does not start with a word')
