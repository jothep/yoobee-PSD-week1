import random
import nltk
from nltk.corpus import words as nltk_words

class Hangman:
    def __init__(self, word_list=None, max_fails=5, max_len=5):
        self.max_fails = max_fails
        self.fails = 0
        self.guessed_letters = set()

        if word_list is None:
            try:
                pool = nltk_words.words()
            except LookupError:
                nltk.download('words', quiet=True)
                pool = nltk_words.words()
        else:
            pool = word_list

        self.word_pool = list({w.lower() for w in pool if w.isalpha() and len(w) <= max_len})
        if not self.word_pool:
            raise ValueError("Word list is empty.")
        
        self.random_word = self._generate_random_word(self.word_pool)
        self.blanks = self._generate_blank(self.random_word)

        print(f"Word length: {len(self.random_word)}")
        print("Initial blanks:", " ".join(self.blanks))

    def _generate_random_word(self, word_list):
        return random.choice(word_list)

    def _generate_blank(self, input_str):
        return ["_" for _ in input_str]

    def _check_if_letter_exists(self, letter):
        correct = False
        for i, ch in enumerate(self.random_word):
            if ch == letter:
                self.blanks[i] = letter
                correct = True
        return correct

    def _get_valid_guess(self):
        while True:
            guess = input("Enter a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
            elif guess in self.guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter.")
            else:
                return guess
        
    def _process_guess(self, letter):
        if self._check_if_letter_exists(letter):
            print(f"Correct guess for '{letter}'.")
        else:
            self.fails += 1
            print(f"Wrong guess for letter '{letter}'.")
        print("Word:", " ".join(self.blanks))

    def play(self):
        while "_" in self.blanks and self.fails < self.max_fails:
            print(f"Fails: {self.fails}/{self.max_fails} | Guessed: {' '.join(sorted(self.guessed_letters))}")
            guess = self._get_valid_guess()
            self.guessed_letters.add(guess)
            self._process_guess(guess)

        if "_" not in self.blanks:
            print(f"You win! The word was '{self.random_word}'")
        else:
            print(f"You lose! The word was '{self.random_word}'")

if __name__ == "__main__":
    game = Hangman(max_fails=5, max_len=5)
    game.play()