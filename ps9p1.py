def onlyallowschars(inputstring):
  allowedchars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
  return all(char in allowedchars for char in inputstring)

teststring1 = "ABCDEFabcdef123450"
teststring2 = "*&%@#!}{"

result1 = onlyallowschars(teststring1)
result2 = onlyallowschars(teststring2)

print(result1)
print(result2)

