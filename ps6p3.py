def translatenum(phonenum):
  translatednum = ''
  for char in phonenum:
      if char.isdigit():
          translatednum += char
      elif char.isalpha():
          char = char.upper()
          if char >= 'A' and char <= 'C':
              translatednum += '2'
          elif char >= 'D' and char <= 'F':
              translatednum += '3'
          elif char >= 'G' and char <= 'I':
              translatednum += '4'
          elif char >= 'J' and char <= 'L':
              translatednum += '5'
          elif char >= 'M' and char <= 'O':
              translatednum += '6'
          elif char >= 'P' and char <= 'S':
              translatednum += '7'
          elif char >= 'T' and char <= 'V':
              translatednum += '8'
          elif char >= 'W' and char <= 'Z':
              translatednum += '9'
      else:
          translatednum += char
  return translatednum

# Get user input for telephone number
phonenum = input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")

# Translate and display the number
translatednum = translatenum(phonenum)
print("Translated telephone number:", translatednum)

