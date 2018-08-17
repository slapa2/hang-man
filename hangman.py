import random
from fild import Fild


class Game:
    def __init__(self, win_result, max_mishits):
        self.win_result = win_result
        self.max_mishits = max_mishits
        self.result = [0, 0]
        self.player = 0
        self.win = False
        self.fild = Fild()
        self.round = Round()
        self.game_start()

    def game_start(self):

        while not self.win:
            self.round.new_round()
            self.fild.print_fild(self)
            end_round_str = ''

            while self.round.mishit_counter < self.max_mishits and not self.round.win_round:
                self.round.take_letter()
                self.fild.print_fild(self)
                if self.round.check_round_win():
                    self.result[self.player] += 1
                    end_round_str = '\nZgadłeś!'
                elif self.round.mishit_counter == self.max_mishits:
                    end_round_str = '\nNiestety wisisz!\nHasło to: {}'.format(self.round.word)

            input(end_round_str)
            if self.result[self.player] == self.win_result:
                self.win = True
                input('Wygrywa gracz ' + str(self.player + 1))
                self.game_start()
            self.change_player()

    def change_player(self):
        self.player = int(not self.player)


class Round:

    def __init__(self):
        self.word = ''
        self.letters = []
        self.mishit_counter = 0
        self.win_round = False

    def new_round(self):
        self.word = self.get_random_word()
        self.letters = []
        self.mishit_counter = 0
        self.win_round = False

    def get_random_word(self):
        words = ['taboret', 'kwiatek', 'mlotek']
        return random.choice(words)

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
            if letter in self.letters:
                masked_word += letter
            else:
                masked_word += ' _ '
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
    game = Game(int(win_result), int(max_mishits))
