import re

text = 'Python      Exercises'

result = re.sub(r'\s+', ' ', text)

print("Original text:", text)
print("Text with multiple spaces removed:", result)
