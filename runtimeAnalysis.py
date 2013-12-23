#! /usr/bin/python
import tarrasque
from pprint import pprint

class Replay:
	def __init__(self):
		print("Initializing replay class.")
		#initialize players and their heros as objects
		self.playerPositions = dict()
		self.itemList = []

	def loadReplay(self, fileName):
		self.replay = tarrasque.StreamBinding.from_file(fileName)
		print("Replay fully parsed.")

	def initializeHeroDict(self):
		for player in self.replay.players:
			hero = player.hero
			heroName = hero.name
			initPosition = hero.position
			self.playerPositions[heroName] = [initPosition]
		for entry in self.playerPositions:
			print(entry)

	def timeStepAndLocation(self, stepSize):
		self.replay.go_to_tick(self.replay.tick + stepSize)
		for player in self.replay.players:
			hero = player.hero
			heroName = hero.name
			pos = hero.position
			self.playerPositions[heroName].append(pos)
		for entry in self.playerPositions:
			print(entry)

	def itemsPurchased(self):
		for player in self.replay.players:
			for item in player.hero.inventory:
				self.itemList.append((item, item.purchase_time))
		for item in self.itemList:
			print(item)
				

def test():
	replayClass = Replay() 
	replayClass.loadReplay("test.dem")
	replayClass.initializeHeroDict()
	replayClass.timeStepAndLocation(1)
	replayClass.itemsPurchased()

def parse(command):
	if command == "q":
		exit(0)

	elif command == "h":
		print("q - quit\n intialize - Initialize a replay class\n loadReplay - Load a replay for analysis")

	elif command == "initialize":
		replayClass = Replay()

	elif command == "loadReplay":
		replayClass.loadReplay("test.dem")
	
	elif command == "initializeHeroDict":
		replayClass.initializeHeroDict()

	elif command == "test":
		test()	

	else:
		print("Command was not recognized. Enter -h for a list of commands.")
	

if __name__=='__main__':
	while True:
		command = raw_input("Please enter a command: ")
		parse(command)
