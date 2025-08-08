import random
import nltk
nltk.download('words')
from nltk.corpus import words

def generate_random_word(word_list):
    random_word = random.choice(word_list)
    print(random_word)
    return random_word.lower()

def generate_blank(input_str):
    blanks = ["_" for _ in input_str]
    print("Initial blanks:", " ".join(blanks))
    return blanks

def check_if_letter_exists(letter, word, blanks):
    correct = False
    for i in range(len(word)):
        if word[i] == letter:
            blanks[i] = letter
            correct = True
    print("Updated blanks:", " ".join(blanks))
    return correct, blanks

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
        else:
            return guess
        
def process_guess(letter, word, blanks, fails):
    correct, updated_blanks = check_if_letter_exists(letter, word, blanks)
    if correct:
        print(f"Correct guess for '{letter}'.")
    else:
        fails += 1
        print(f"Wrong guess for letter '{letter}'.")
    print("Word:", " ".join(updated_blanks))
    return updated_blanks, fails

if __name__ == "__main__":
    word_list = words.words()
    word_list_5l = [w.lower() for w in word_list if w.isalpha() and len(w) <= 5]
    random_w = generate_random_word(word_list_5l)
    blanks = generate_blank(random_w)

    max_fails = 5
    fails = 0
    guessed_letters = set()

    while "_" in blanks and fails < max_fails:
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        blanks, fails = process_guess(guess, random_w, blanks, fails)

    if "_" not in blanks:
        print(f"You win! The word was '{random_w}'")
    else:
        print(f"You lose! The word was '{random_w}'")
 