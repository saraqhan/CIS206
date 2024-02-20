def operation(number1, number2, operation_code):
  result = 0
  
  if operation_code == 'A':
    result = number1 + number2
  elif operation_code == 'S':
    result = number1 - number2
  elif operation_code == 'M':
    result = number1 * number2
  elif operation_code == 'D':
    if number2 != 0:
      result = number1 / number2
    else:
      result = -999
      print("Cant divide by 0")
    return result

number1 = float(input("First number: "))
number2 = float(input("Second number: "))
operation_code = input("Operation code (A,S,M,D): ")

result = operation(number1, number2, operation_code)

print("Number 1: ", number1)
print("Number 2: ", number2)
print("Operation code: ", operation_code)
print("Result: ", result)