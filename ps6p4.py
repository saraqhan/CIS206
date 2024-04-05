def countvowels(string):
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
      if char in vowels:
          count += 1
  return count

def countcons(string):
  consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  count = 0
  for char in string:
      if char in consonants:
          count += 1
  return count

# Get user input for a string
user_input = input("Enter a string: ")

# Count vowels and consonants
num_vowels = countvowels(user_input)
num_consonants = countcons(user_input)

# Display the counts
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
