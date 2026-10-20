import random

# ---------------------------------------
# 1. LOAD WORDS FROM THE PROVIDED FILE
# ---------------------------------------

try:
    with open("google-10000-english-no-swears.txt", "r",
              encoding="utf-8") as file:
        words = [
            line.strip().upper()
            for line in file
            if line.strip().isalpha() and len(line.strip()) >= 4
        ]
except FileNotFoundError:
    print("Error: Word-list file not found!")
    print("Keep the TXT file in the same folder as hangman.py.")
    raise SystemExit

if not words:
    print("Error: No suitable words found in the file.")
    raise SystemExit


# ---------------------------------------
# 2. HANGMAN ASCII DRAWINGS
# ---------------------------------------

stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


# ---------------------------------------
# 3. START THE HANGMAN GAME
# ---------------------------------------

def play_hangman(secret_word_override=None):

    secret_word = secret_word_override.upper() if secret_word_override else random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n" + "=" * 40)
    print("          HANGMAN WORD GAME")
    print("=" * 40)
    print("Guess the hidden word, one letter at a time!")
    print("You can make a maximum of 6 incorrect guesses.")
    print("Let's start!\n")

    # -----------------------------------
    # 4. REPEAT UNTIL WIN OR DEFEAT
    # -----------------------------------

    while True:

        # Display the correct hangman stage
        print(stages[wrong_guesses])

        # Display the hidden word
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)
        print("Guessed letters:",
              " ".join(sorted(guessed_letters)) or "None")
        print("Incorrect guesses:",
              wrong_guesses, "/", max_wrong_guesses)

        # --------------------------------
        # 5. CHECK FOR VICTORY
        # --------------------------------

        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 40)
            print("       CONGRATULATIONS!")
            print("          YOU WIN!")
            print("=" * 40)
            print("The correct word was:", secret_word)
            break

        # --------------------------------
        # 6. CHECK FOR DEFEAT
        # --------------------------------

        if wrong_guesses >= max_wrong_guesses:
            print("\n" + "=" * 40)
            print("          GAME OVER!")
            print("          YOU LOSE!")
            print("=" * 40)
            print("The correct word was:", secret_word)
            break

        # --------------------------------
        # 7. GET A LETTER FROM THE PLAYER
        # --------------------------------

        guess = input("\nEnter one letter: ").strip().upper()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter one letter only.\n")
            continue

        # --------------------------------
        # 8. PREVENT DUPLICATE GUESSES
        # --------------------------------

        if guess in guessed_letters:
            print("You already guessed that letter!")
            print("Try a different letter.\n")
            continue

        guessed_letters.add(guess)

        # --------------------------------
        # 9. CHECK THE LETTER
        # --------------------------------

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess! Be careful.\n")


# ---------------------------------------
# 10. RUN THE GAME
# ---------------------------------------

if __name__ == "__main__":
    play_hangman()

    