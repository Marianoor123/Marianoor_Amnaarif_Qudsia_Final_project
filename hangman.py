#code by Qudsia (lines 2-16)
import random

def hangman():

    words = ["pakistan", "korea", "japan", "china", "malaysia", "indonesia"]
    
    while True:  
        word = random.choice(words)
        guessed_word = ["_"] * len(word)
        attempts = 6
        guessed_letters = []

        print("Welcome to Hangman!")
        print("The word has", len(word), "letters.")
        print(" ".join(guessed_word))

#code by Maria Noor (lines 18-28)
        while attempts > 0:
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
#code by Amna Arif (lines 29-54)

            guessed_letters.append(guess)

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                print("Correct!", " ".join(guessed_word))
            else:
                attempts -= 1
                print(f"Incorrect! {attempts} attempts remaining.")

            if "_" not in guessed_word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Out of attempts! The word was:", word)


        play_again = input("Do you want another player to play? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break  

hangman()