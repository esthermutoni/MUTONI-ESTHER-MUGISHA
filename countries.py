nation_list = ["ghana", "nigeria", "ethiopia", "zambia", "namibia"]

print("Welcome to the Country Guessing Challenge!")
print("Try to guess one of the countries in my list.")
print()

max_guesses = 5
guess_count = 0
is_winner = False

while guess_count < max_guesses:
    user_guess = input("Enter your guess: ").strip().lower()

    if not user_guess:
        print("Country name cannot be empty.")
        continue

    guess_count += 1

    if user_guess in nation_list:
        print(f"Well done! '{user_guess}' is one of the countries.")
        is_winner = True
        break

    guesses_left = max_guesses - guess_count
    if guesses_left > 0:
        print(f"Incorrect guess. You have {guesses_left} attempt(s) remaining.")
    else:
        print("No attempts left. Game over!")

if is_winner:
    print(f"Congratulations! You guessed correctly after {guess_count} attempt(s).")
else:
    print(f"One possible correct answer was: {nation_list[0]}")