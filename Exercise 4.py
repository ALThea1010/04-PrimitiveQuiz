# Dictionary containing 10 European countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Greece": "Athens",
    "Sweden": "Stockholm",
    "Norway": "Oslo"
}

# Initialize score
score = 0

# Function to check the user's guess
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:  # Allow two more attempts
                guess = input("Sorry, wrong answer. Try again: ")
            attempt += 1
    
    if attempt == 3:
        print(f"The correct answer is {answer}.")

# Main quiz loop
print("Guess the capitals of the following countries:")
# Iterate over the countries and ask each question separately
for country, capital in quiz.items():
    guess = input(f"What is the capital of {country}? ")  # Ask each country separately
    check_guess(guess, capital)

# Print the final score after the quiz is over
print(f"Your final score is {score} out of {len(quiz)}.")


