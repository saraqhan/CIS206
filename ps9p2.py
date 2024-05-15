import re

pattern = re.compile(r'^ab*$')

teststrings = ["ab", "abc", "a", "ab", "abb"]

for teststring in teststrings:
    if pattern.match(teststring):
        print(f'"{teststring}" matches the pattern')
    else:
        print(f'"{teststring}" does not match the pattern')

