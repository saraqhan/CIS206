side1 = float(input("Side 1: "))
side2 = float(input("side 2: "))
side3 = float(input("side 3: "))

if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
  print("This is a right triangle")
else:
  print("This is not a right triangle")