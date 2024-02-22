while True:
  try:
    user_input = int(input("Enter a integer between 10 and 20: "))
    if 10 <= user_input <= 20:
      break
    else:
      print("input not accepted, try again")
  except ValueError:
    print("input not accepted, try again")

for i in range(user_input + 1):
  print(i)