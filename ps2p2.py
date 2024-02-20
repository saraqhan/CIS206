def calculator(num1, num2, operation):
  if operation == '+':
    result = num1 + num2
  elif operation == '-':
    result = num1 - num2
  elif operation == '*':
    result = num1 * num2
  elif operation == '/':
    if num2 !=0:
      result = num1 / num2
    else:
      return "Error: Division by zero is not allowed."
  else:
    return "Error: Invalid operation."
  return result

num1 = float(input("Enter the first number: "))

num2 = float(input("enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")