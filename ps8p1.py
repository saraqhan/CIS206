def main():
  rf = []
  for month in range(1, 13):
      rf.append(float(input(f"rainfall for month {month}: ")))

  ttlrf = sum(rf)
  avgrf = ttlrf / 12

  maxrfmonth = rf.index(max(rf)) + 1
  minrfmonth = rf.index(min(rf)) + 1

  print("\nrainfall statistics:")
  print(f"total rainfall for the year: {ttlrf} inches")
  print(f"average monthly rainfall: {avgrf} inches")
  print(f"month(s) with the highest rainfall: month {maxrfmonth}")
  print(f"month(s) with the lowest rainfall: month {minrfmonth}")

if __name__ == "__main__":
  main()
