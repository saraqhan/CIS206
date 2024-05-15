import re

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

pattern = re.compile(r'\b[ae]\w*')

wordsstartingwithaore = pattern.findall(text)

print("Words starting with 'a' or 'e':", wordsstartingwithaore)
