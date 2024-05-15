def main():
  numbers = []
  for i in range(20):
      num = float(input(f"enter number {i+1}: "))
      numbers.append(num)

  lowest = min(numbers)
  highest = max(numbers)
  total = sum(numbers)
  average = total / len(numbers)

  print("\nnumber analysis:")
  print(f"lowest number: {lowest}")
  print(f"highest number: {highest}")
  print(f"total of numbers: {total}")
  print(f"average of numbers: {average}")

if __name__ == "__main__":
  main()
