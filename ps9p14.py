import re

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

words_starting_with_a_or_e = re.findall(r'\b[ae]\w*', text)

print("Words starting with 'a' or 'e':", words_starting_with_a_or_e)
