import random
from field import Field
from words import Words


class Game:

    def __init__(self, win_result, max_mishits, words):
        self.win_result = win_result
        self.max_mishits = max_mishits
        self.words = words
        self.result = [0, 0]
        self.player = 0
        self.win = False
        self.field = Field()
        self.round = Round(self.words)
        self.game_start()

    def game_start(self):

        while not self.win:
            self.round.new_round()
            self.field.print_fild(self)
            end_round_str = ''

            while self.round.mishit_counter < self.max_mishits and not self.round.win_round:
                self.round.take_letter()
                self.field.print_fild(self)
                if self.round.check_round_win():
                    self.result[self.player] += 1
                    end_round_str = '\nZgadłeś!'
                elif self.round.mishit_counter == self.max_mishits:
                    end_round_str = '\nNiestety wisisz!\nHasło to: {}'.format(
                        self.round.word)

            input(end_round_str)
            if self.result[self.player] == self.win_result:
                self.win = True
                input('Wygrywa gracz ' + str(self.player + 1))
                self.game_start()
            self.change_player()

    def change_player(self):
        self.player = int(not self.player)


class Round:

    def __init__(self, words):
        self.words = words
        self.word = ''
        self.letters = []
        self.mishit_counter = 0
        self.win_round = False

    def new_round(self):
        self.word = self.get_random_word()
        self.letters = [' ']
        self.mishit_counter = 0
        self.win_round = False

    def get_random_word(self):
        return random.choice(self.words)

    def take_letter(self):
        letter = self.get_letter()
        self.letters.append(letter)
        if letter not in self.word:
            self.mishit_counter += 1

    def get_letter(self):
        letter = input('\nPodaj literę: ')
        while not letter.isalpha() or len(letter) != 1:
            if letter.lower() in ['exit', 'exit()', 'koniec']:
                exit()
            letter = input('\nPodaj poprawną literę: ')

        letter = letter.lower()
        if letter in self.letters:
            print("Tą literę już podałeś!")
            letter = self.get_letter()
        return letter

    def check_round_win(self):
        if set(list(self.word)) <= set(self.letters):
            self.win_round = True
        return self.win_round

    def get_masked_word(self):
        masked_word = ''
        for letter in self.word:
            if letter not in self.letters:
                letter = '_'
            masked_word += ' ' + letter
        return masked_word


if __name__ == '__main__':

    print("""     _____  _____  _____  _____  _____  _____  _____ 
    |  |  ||  _  ||   | ||   __||     ||  _  ||   | |
    |     ||     || | | ||  |  || | | ||     || | | |
    |__|__||__|__||_|___||_____||_|_|_||__|__||_|___|\n""")

    win_result = input("Do ilu wygranych grancie? max (1-99)")
    while not win_result.isdecimal() or int(win_result) < 1 or int(win_result) > 99:
        win_result = input("Podaj poprawną liczbę! ")

    max_mishits = input("Do ile pudeł kończy rundę? (1-11) ")
    while not max_mishits.isdecimal() or int(max_mishits) < 1 or int(max_mishits) > 11:
        max_mishits = input("Podaj poprawną liczbę! ")

    win_result, max_mishits = int(win_result), int(max_mishits)

    words = Words()

    max_word_len = input("jak długie mogą być słowa? (minimalnie: {} maksymalnie: {}) ".format(
        words.min_len, words.max_len))

    while not max_word_len.isdecimal() or int(max_word_len) < words.min_len or int(max_word_len) > words.max_len:
        max_word_len = input("Podaj poprawną liczbę! ")
    max_word_len = int(max_word_len)

    min_word_len = input("jak krótnie mogą być słowa? (minimalnie: {} maksymalnie: {}) ".format(
        words.min_len, max_word_len))
    while not min_word_len.isdecimal() or int(min_word_len) < words.min_len or int(min_word_len) > max_word_len:
        min_word_len = input("Podaj poprawną liczbę! ")

    min_word_len = int(min_word_len)

    print(min_word_len, max_word_len)

    game = Game(win_result, max_mishits,
                words.get_words(min_word_len, max_word_len))
