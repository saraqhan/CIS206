fr1 = 5000
fr2 = 20000
rr2 = 0.125
rr3_first_4000 = 0.10
rr3_over_4000 = 0.14

net = float(input("Price of one copy of novel: "))
est_copies_sold = int(input(
"Copies estimated to be sold: "
))
royalty1 = fr1 + fr2
print("With option 1, you will get $", royalty1, "in total.")

royalty2 = net * rr2 * est_copies_sold
print("with option 2, you'd get $", royalty2, "in total.")

if est_copies_sold <= 4000:
  royalty3 = net * rr3_first_4000 * est_copies_sold
else:
  royalty3 = (net * rr3_first_4000 * 4000) + (net * rr3_over_4000 * (est_copies_sold - 4000))
print("With option 3, you'd get $", royalty3, "in total.")

best_option = max(1,2,3,key=lambda option: eval("royalty" + str(option)))
print("The best option is option", best_option, "with total royalties of $", eval("royalty_option_" + str(best_option)))