#! /usr/bin/python
import tarrasque

def analyzeReplay():
	replay = tarrasque.StreamBinding.from_file("test.dem")

def parse(command):
	if command == "-q":
		exit(0)

	elif command == "-h":
		print("Still need to implement this.")

	elif command == "-ar":
		analyzeReplay()	

	else:
		print("Command was not recognized. Enter -h for a list of commands.")


if __name__=='__main__':
	while True:
		command = raw_input("Please enter a command: ")
		parse(command)		
