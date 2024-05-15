def replace_whitespace(text):
  return text.replace(' ', '_')

def replace_underscore(text):
  return text.replace('_', ' ')

text1 = "Regular Expressions"
text2 = "Code_Examples"

result1 = replace_whitespace(text1)
result2 = replace_whitespace(text2)
print("Result 1:", result1)
print("Result 2:", result2)

result3 = replace_underscore(result1)
result4 = replace_underscore(result2)
print("Result 3:", result3)
print("Result 4:", result4)
