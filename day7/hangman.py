import random

word_list = ["ardvark", "baboon", "camel"]

# todo 1: randomly choose a word from word_list and assign it to variable chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
lives = 6

for letter in chosen_word:
    placeholder += "_"


# todo 3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word. If it is, print "Right". Otherwise, print "Wrong".
# continue the loop until the user guesses all the letters in the chosen_word and then print "You win." OR they run out of lives and print "You lose."
while placeholder != chosen_word:
    # todo 2: ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print("Right")
        # a letter can be used multiple times in a word, so we need to check for all occurrences of the guessed letter in the chosen_word and update the placeholder accordingly.
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                placeholder = placeholder[:position] + letter + placeholder[position + 1:]

    else:
        print("Wrong")
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            print("You lose.")
            break

    print(placeholder)

if placeholder == chosen_word:
    print("You win.")
