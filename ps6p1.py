def lowercase(fulln):
  firstn, lastn = fulln.split()
  firstn = firstn.capitalize()
  lastn = lastn.capitalize()
  cap_fulln = firstn + ' ' + lastn
  return cap_fulln

fulln = input("Enter first name and last name: ")
lowercased_name = lowercase(fulln)
print("Full name:", lowercased_name)

