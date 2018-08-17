import os
from math import ceil

class Fild:
    def __init__(self):
        self.fild = """                                            
     _____  _____  _____  _____  _____  _____  _____ 
    |  |  ||  _  ||   | ||   __||     ||  _  ||   | |
    |     ||     || | | ||  |  || | | ||     || | | |
    |__|__||__|__||_|___||_____||_|_|_||__|__||_|___|  
_________________________________________________________
|                                                       |
| player 1              {} : {}             player 2    |
|_______________________________________________________|
|  gracz: {}                                pudła: {}/{} |
{}
| hasło: {}|
|_______________________________________________________|
|         |                                             |
| litery  | {} |
|_________|_____________________________________________|
aby zakończyć gerę wpisz: \"exit\""""

        self.hangmans = [
            '''|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |''',
            '''|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                           _ _                         |
|                                                       |''',
            '''|                                                       |
|                            |                          |
|                            |                          |
|                            |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',
            '''|                                                       |
|                           \|                          |
|                            |                          |
|                            |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',
            '''|                         ____                          |
|                           \|                          |
|                            |                          |
|                            |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',
            '''|                         ____                          |
|                        |  \|                          |
|                            |                          |
|                            |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',
            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                            |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',
            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                        |   |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',

            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                       /|   |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',

            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                       /|\  |                          |
|                            |                          |
|                           _|_                         |
|                                                       |''',

            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                       /|\  |                          |
|                       /    |                          |
|                           _|_                         |
|                                                       |''',

            '''|                         ____                          |
|                        |  \|                          |
|                        o   |                          |
|                       /|\  |                          |
|                       / \  |                          |
|                           _|_                         |
|                                                       |'''
    ]

    def _getHangman(self, mishits, maxMishits):
        return self.hangmans[ceil(mishits * (11/maxMishits))]

    def printFild(self, game):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(
            self.fild.format(
                str(game.result[0]).rjust(2),
                str(game.result[1]).ljust(2),
                str(game.player + 1),
                str(game.round.mishitCounter).rjust(2),
                str(game.maxMishits).ljust(2),
                self._getHangman(game.round.mishitCounter, game.maxMishits),
                game.round.getMaskedWord().ljust(47),
                ' '.join(sorted(game.round.letters)).ljust(43)
            )
        )
