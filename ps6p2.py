def only_initials(fulln):
  names = fulln.split()
  
  initials = [name[0].upper() + '.' for name in names]

  return ' '.join(initials)

fulln = input("Enter first, middle, and last name: ")

initials = only_initials(fulln)
print("Initials:", initials)