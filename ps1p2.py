def compute(number):
  result = number * 10
  print("10 times " + str(number) + " is: " + str(result))

numbers = [100, 1000, 10000]

for num in numbers:
  compute(num)