def calc_reward_pts(pts, redemption_code):
  if redemption_code == 'C':
    reward_pts = 2 * pts
  elif redemption_code == 'X':
    reward_pts = 3 * pts
  else:
    reward_pts = 1.5 * pts
  return reward_pts

pts = float(input("Number of points earned: "))
redemption_code = input("Redemption code (C, X, or others): ")
reward_pts = calc_reward_pts(pts, redemption_code)

print("Reward points earned: ", reward_pts)
print("Redemption code: ", redemption_code)
print("Reward points:", reward_pts)