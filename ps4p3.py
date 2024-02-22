fav_names = ["angel", "matthew", "alexa", "habib", "allexus", "justin", "dylan", "zoya", "eric", "zhandos"]

while True:
  user_input = input("Enter a name: ")
  if user_input in fav_names:
    print(user_input, "is one of my favorite names!")
    break
  else:
    print(user_input, "is not one of my favorite names. try again!!")