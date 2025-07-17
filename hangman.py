import random

# Word list and choosing a word
word_list = ["banana", "elephant", "python", "hangman"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game variables
lives = 6
game_over = False
correct_letters = []
guessed_letters = []

# Initial placeholder print
placeholder = ""
for position in range(word_length):
    placeholder += " "
print(" Word to guess:", placeholder)

# Main game loop
while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        print(" Correct guess!")
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f" Wrong guess! Lives left: {lives}")
        if lives == 0:
            print("\n Game Over! The word was:", chosen_word)
            break

    # Update display
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += " "

    print("Current word:", display)
    print("Guessed letters so far:", ', '.join(guessed_letters))

    if display == chosen_word:
        print("\n You guessed the word correctly!")
        game_over = True
