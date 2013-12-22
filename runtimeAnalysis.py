#! /usr/bin/python
import tarrasque

class Replay:
	def __init__(self):
		print("Initializing replay class.")

	def loadReplay(fileName):
		self.replay = tarrasque.StreamBinding.from_file(fileName)
		print("Replay fully parsed.")

def parse(command):
	if command == "q":
		exit(0)

	elif command == "h":
		print("q - quit\n intialize - Initialize a replay class\n loadReplay - Load a replay for analysis")

	elif command == "initialize":
		replay = Replay()

	elif command == "loadReplay":
		replay.loadReplay("test.dem")	

	else:
		print("Command was not recognized. Enter -h for a list of commands.")


if __name__=='__main__':
	while True:
		command = raw_input("Please enter a command: ")
		parse(command)		
