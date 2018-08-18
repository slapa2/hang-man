import os
from math import ceil


class Field:
    def __init__(self):
        self.field = """                                            
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

    def _get_hangman(self, mishits, max_mishits):
        return self.hangmans[ceil(mishits * (11/max_mishits))]

    def print_fild(self, game):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            self.field.format(
                str(game.result[0]).rjust(2),
                str(game.result[1]).ljust(2),
                str(game.player + 1),
                str(game.round.mishit_counter).rjust(2),
                str(game.max_mishits).ljust(2),
                self._get_hangman(game.round.mishit_counter, game.max_mishits),
                game.round.get_masked_word().ljust(47),
                ''.join(sorted(game.round.letters[1:])).ljust(43)
            )
        )
