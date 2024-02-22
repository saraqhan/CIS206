def calc(score1, score2):
    total_pts = 0.6 * score1 + 0.4 * score2
    return total_pts

def valid_score(score):
    return 0 <= score <= 100

def main():
    user_input = input("Do you want to do the program?: ")

    while user_input.lower() == "yes":
        score1 = float(input("Enter score 1: "))
        score2 = float(input("Enter score 2: "))

        if not (valid_score(score1) and valid_score(score2)):
            print("Invalid score")
            user_input = input("Do you want to redo the program?: ")
            continue

        ttl_pts = calc(score1, score2)
        print(f"Total points: {ttl_pts}")
        user_input = input("Do you want to do the program?: ")

    print("Thank you for using the program.")

if __name__ == "__main__":
    main()
