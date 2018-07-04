import Word
import os
import random

class Game:
	def __init__(self):
		self.result = [0,0]
		self.player = 0
		self.winResult = 2
		self.maxMishits = 5
		self.win = False
		while not self.win:
			round = Round()
			self.printFild(round)
			while round.mishitCounter < self.maxMishits and not round.winRound:
				round.takeLeter()
				self.printFild(round)
				if round.chechRoundWin():
					self.result[self.player] += 1
					print('Zgadłeś!')
					input()
				elif round.mishitCounter == self.maxMishits:
					print('Niestety wisisz!')
					input()
					
				self.changePlayer()
					
		if self.result[self.player] == self.winResult:
			self.win = True
			print('Wygrywa gracz ' + str(self.player + 1))

	def changePlayer(self):
		self.player = int(not self.player)

	def printFild(self,  round):
		os.system('cls')
		print('playr 1: ' + str(self.result[0]) + '\t\t\tplayr 2: ' + str(self.result[1]))
		print('\nplayr ' + str(self.player + 1) + '\t\t\t\tpudła: ' + str(round.mishitCounter) + '/' + str(self.maxMishits) + '\n\n')
		print(round.printHangman())
		round.printMaskedWord()
		print('\nLitery: ' + ' '.join(sorted(round.leters)))

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
		while leter in self.leters:
			leter = input('\nPodaj literę: ')
		self.leters.append(leter)

		if leter not in self.word:
			self.mishitCounter += 1

	def chechRoundWin(self):
		if set(list(self.word)) <= set(self.leters):
			self.winRound = True
		return self.winRound

	def printMaskedWord(self):
		maskedWord = ''
		for leter in self.word:
			if leter in self.leters:
				maskedWord += leter
			else:
				maskedWord += ' _ '
		print(maskedWord)

	def printHangman(self):

		hangmans = [
'''		     
		      
		      
		      
		      
		       \n''',
'''		     
		     |
		     |
		     |
		     |
		    _|_\n''',
'''		 ____
		    \|
		     |
		     |
		     |
		    _|_\n''',
'''		 ____
		 |  \|
		 o   |
		     |
		     |
		    _|_\n''',
'''		 ____
		 |  \|
		 o   |
		/|\  |
		     |
		    _|_\n''',
					
'''		 ____
		 |  \|
		 o   |
		/|\  |
		/\   |
		    _|_\n'''
		]
		return hangmans[self.mishitCounter]
		


if __name__ == '__main__':
	game = Game()
