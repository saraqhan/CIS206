def calculate(weight, zipcode, area, weight_charge):
  area_table = {
    60171: 2.00,
    60172: 2.50,
    60635: 3.00,
  }

weight_table = {
  100: 0.02,
50: 0.03
}

if zipcode in area_table:
  area[0] =  area_table[zipcode]
else:
  area[0] = 5.00

if weight > 100:
  weight_charge[0] = weight * weight_table[100]
elif weight > 50:
  weight_charge[0] = weight * weight_table[50]
else:
  weight_charge[0] = weight * 0.05

postage[0] = area[0] + weight_charge[0]

return weight_charge[0], area[0], postage[0]

weight = float(input("Enter the weight of the package: "))
zipcode = int(input("Enter the zipcode: "))

area = [0]
weight_charge = [0]
postage = [0]

weight_charge_result, area_charge_result, postage_result = calculate_postage(weight, zip_code, area_charge, weight_charge)

print("Area charge: $", area_charge_result)
print("Weight charge: $", weight_charge_result")
print("Postage: $", postage_result)