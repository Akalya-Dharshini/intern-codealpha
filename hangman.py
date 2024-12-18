import random

def display_hangman(tries):
    stages = [
        """
        ---------
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
        ---------
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
        ---------
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
        ---------
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
        ---------
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
        ---------
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
        ---------
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]

def choose_word():
    words = ["python", "javascript", "hangman", "developer", "programming", "algorithm"]
    return random.choice(words)

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
                word_completion = " ".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Invalid input. Please guess a single letter.")

        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"You ran out of tries. The word was '{word}'. Better luck next time!")

if __name__ == "__main__":
    hangman()
