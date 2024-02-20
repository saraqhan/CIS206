def rewards(pts, redemption_code):
  multiplier = {
    'C': 2,
    'X': 3
  }

rewards_pts = pts * multiplier.get(redemption_code, 1.5)

dv = rewards_pts *  1.50

return rewards_pts, dv

pts = float(input("Enter the number of points: "))
redemption_code = input("Enter the redemption code(C, X, or other): ")
rewards_pts_result, dv_result = rewards(pts, redemption_code)

print("points", pts)
print("redemption code", redemption_code)
print("rewards points", rewards_pts_result)
print("dollar value: $", dv_result)