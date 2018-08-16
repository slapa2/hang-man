import random
from fild import Fild


class Game:
    def __init__(self):
        self.winResult = 2
        self.maxMishits = 9
        self.result = [0, 0]
        self.player = 0
        self.win = False
        self.fild = Fild()
        self.round = Round()
        self.gameStart()

    def gameStart(self):

        while not self.win:
            self.round.newRound()
            self.fild.printFild(self)
            endRoundStr = ''

            while self.round.mishitCounter < self.maxMishits and not self.round.winRound:
                self.round.takeLeter()
                self.fild.printFild(self)
                if self.round.chechRoundWin():
                    self.result[self.player] += 1
                    endRoundStr = '\nZgadłeś!'
                elif self.round.mishitCounter == self.maxMishits:
                    endRoundStr = '\nNiestety wisisz!\nHasło to: {}'.format(self.round.word)

            input(endRoundStr)
            if self.result[self.player] == self.winResult:
                self.win = True
                input('Wygrywa gracz ' + str(self.player + 1))
                self.gameStart()
            self.changePlayer()

    def changePlayer(self):
        self.player = int(not self.player)


class Round:

    def __init__(self):
        self.word = self.getRandomWord()
        self.letters = []
        self.mishitCounter = 0
        self.winRound = False

    def newRound(self):
        self.word = self.getRandomWord()
        self.letters = []
        self.mishitCounter = 0
        self.winRound = False

    def getRandomWord(self):
        words = ['taboret', 'kwiatek', 'mlotek']
        return random.choice(words)

    def takeLeter(self):
        letter = input('\nPodaj literę: ')
        if letter in ['exit', 'exit()', 'koniec']:
            exit()
        while letter[0] in self.letters:
            letter = input('\nPodaj nową literę: ')
        self.letters.append(letter[0])

        if letter not in self.word:
            self.mishitCounter += 1

    def chechRoundWin(self):
        if set(list(self.word)) <= set(self.letters):
            self.winRound = True
        return self.winRound

    def getMaskedWord(self):
        maskedWord = ''
        for letter in self.word:
            if letter in self.letters:
                maskedWord += letter
            else:
                maskedWord += ' _ '
        return maskedWord


if __name__ == '__main__':
    game = Game()
