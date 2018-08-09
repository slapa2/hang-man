import os
import random
import fild


class Game:
    def __init__(self):
        self.winResult = 2
        self.maxMishits = 9
        self.hangman = fild.Pictures()
        self.result = [0, 0]
        self.player = 0
        self.win = False
        self.gameStart()

    def gameStart(self):

        while not self.win:
            round = Round()
            self.printFild(round)
            endRoundStr = ''

            while round.mishitCounter < self.maxMishits and not round.winRound:
                round.takeLeter()
                if round.chechRoundWin():
                    self.result[self.player] += 1
                    endRoundStr = '\nZgadłeś!'
                elif round.mishitCounter == self.maxMishits:
                    endRoundStr = '\nNiestety wisisz!'
                self.printFild(round)

            input(endRoundStr)
            if self.result[self.player] == self.winResult:
                self.win = True
                input('Wygrywa gracz ' + str(self.player + 1))
                self.gameStart()
            self.changePlayer()

    def changePlayer(self):
        self.player = int(not self.player)
        print('\a')

    def printFild(self, round):

        os.system('cls' if os.name == 'nt' else 'clear')

        fild = '''[exit]: koniec gry\n
playr 1: {}\t\t\tplayr 2: {}\n
playr {}\t\t\t\tpudła: {}/{}
{}\nHasło:  {}\n\nLitery: {}'''.format(
            str(self.result[0]), str(self.result[1]),
            str(self.player + 1), str(round.mishitCounter), str(self.maxMishits),
            self.hangman.getHangman(round.mishitCounter), round.getMaskedWord(), ' '.join(sorted(round.leters))
        )
        print(fild)


class Round:

    def __init__(self):
        self.word = self.getRandomWord()
        self.leters = []
        self.mishitCounter = 0
        self.winRound = False

    def getRandomWord(self):
        words = ['taboret', 'kwiatek', 'mlotek']
        return random.choice(words)

    def takeLeter(self):
        leter = input('\nPodaj literę: ')
        if leter in ['exit', 'exit()', 'koniec']:
            exit()
        while leter[0] in self.leters:
            leter = input('\nPodaj nową literę: ')
        self.leters.append(leter[0])

        if leter not in self.word:
            self.mishitCounter += 1

    def chechRoundWin(self):
        if set(list(self.word)) <= set(self.leters):
            self.winRound = True
        return self.winRound

    def getMaskedWord(self):
        maskedWord = ''
        for leter in self.word:
            if leter in self.leters:
                maskedWord += leter
            else:
                maskedWord += ' _ '
        return maskedWord


if __name__ == '__main__':
    game = Game()
