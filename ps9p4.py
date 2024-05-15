import re

pattern = re.compile(r'[a-z]+_[a-z]+')

teststrings = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]

for teststring in teststrings:
    if pattern.search(teststring):
        print(f'"{teststring}" contains letters joined by an underscore')
    else:
        print(f'"{teststring}" does not contain letters joined by an underscore')
