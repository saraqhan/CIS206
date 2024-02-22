attempts = 0

while attempts < 3:
  try:
    user_input = int(input("Enter a number between 10 and 20: "))
    if 10 <= user_input <= 20:
     break
    else:
      print("Invalid input. Please try again.")
      attempts += 1
  except ValueError:
    print("Invalid input. Please try again.")
    attempts += 1

if attempts == 3:
  print("You have exceeded the maximum number of attempts.")
else:
  for i in range(user_input + 1):
    print(i)