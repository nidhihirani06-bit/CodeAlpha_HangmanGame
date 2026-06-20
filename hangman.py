import random

words = ["apple", "tiger", "house", "water", "plant"]

word = random.choice(words)

print(word)
import random

words = ["apple", "tiger", "house", "water", "plant"]

word = random.choice(words)

guessed_word = "_" * len(word)

print(guessed_word)
attempts = 6

print("Attempts:", attempts)
guess = input("Enter a letter: ")

print("You entered:", guess)
if guess in word:
    print("Correct Guess")
else:
    print("Wrong Guess")
    while attempts > 0 and "_" in guessed_word:
        import random

words = ["apple", "tiger", "house", "water", "plant"]

word = random.choice(words)

guessed_word = "_" * len(word)

attempts = 6

print("=== Welcome to Hangman Game ===")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", guessed_word)
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in word:

        new_word = ""

        for i in range(len(word)):
            if word[i] == guess or guessed_word[i] != "_":
                new_word += word[i]
            else:
                new_word += "_"

        guessed_word = new_word

        print("Correct Guess!")

    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n❌ Game Over")
    print("The word was:", word)