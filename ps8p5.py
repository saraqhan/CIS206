import random

statescapitals = {
    "alabama": "montgomery",
    "alaska": "juneau",
    "arizona": "phoenix",
    "arkansas": "little rock",
}

correctcount = 0
incorrectcount = 0

for state in statescapitals:
    capitalguess = input(f"what is the capital of {state}? ")
    if capitalguess.lower() == statescapitals[state]:
        print("correct!")
        correctcount += 1
    else:
        print(f"incorrect. the capital of {state} is {statescapitals[state]}.")
        incorrectcount += 1

print("\nquiz results:")
print(f"correct responses: {correctcount}")
print(f"incorrect responses: {incorrectcount}")
