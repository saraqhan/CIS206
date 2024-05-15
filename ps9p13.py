import re

text = 'Python Exercises, PHP exercises.'

result = re.sub(r'[ ,.]', ':', text)

print("Original text:", text)
print("Modified text:", result)
