#! /usr/bin/python

import tarrasque
import pylab as pl
import numpy as np
import math
import matplotlib.pyplot as plt


class Replay:
    """This class is used to handle the majority of interactions with replays.
    It has a couple of different funtions to initialize the replay and then many
    that run analysis on it."""
    
    def __init__(self):
        print("Initializing replay class.")
        
        #playerPositions is used in initializeHeroDict
        self.playersAndPositions = dict()
        #supportItems is used in measuring gold spent on support items
        self.supportItems = dict()

        #commands to run to initialize
        self.loadReplay("test.dem")
        self.initPlayersAndPositions()
        self.initSupportItems()

    def loadReplay(self, fileName):
        self.replay = tarrasque.StreamBinding.from_file(fileName)
        print("Replay fully parsed.")

    #Removed heroNames. Use players&pos for name lookup.

    def initPlayersAndPostions(self):
        for player in self.replay.players:
            #add each hero and their position array
            self.playersAndPositions[player.hero.name] = []

    def initSupportItems(self):
       self.supportItems = {
               'Observer Ward': 150,
               'Sentry Ward': 200,
               'Dust of Appearance': 180,
               'Smoke of Deceit': 100,
               'Gem of True Sight': 900,
               'Animal Courier': 150,
               'Flying Courier': 220,
               'Headdress': 603,
               'Buckler': 803,
               'Hood of Defiance', 2125,
               'Mekanism': 900,
               'Pipe of Insight': 900,
               'Urn of Shadows': 875,
               'Force Staff': 2250,
               'Blink Dagger': 2150
               }

    def timeStepAndLocation(self, stepSize):
        self.replay.go_to_tick(self.replay.tick + stepSize)
        for player in self.replay.players:
            self.playersAndPositions[player.hero.name].append(player.hero.position)
        
        #Bug checking. Will output a shitton of data
        #for entry in self.playerPositions:
            #print(entry)

    def fullGameHeroLocations(self):
        for tick in self.replay.iter_ticks(start="game", end="postgame"):
            for player in self.replay.players:
                self.playersAndPositions[player.hero.name].append(player.hero.position)

    def playerMovementMap(self, hero_name):
        for player in self.replay.players:
            if player.hero == hero_name:
                for tick in self.replay.iter_ticks(start="game", end="postgame"):
                    if not hero.is_alive:
                        break
                    self.playersAndPositions[player.hero.name].append(player.hero.position)
                xVals = []
                yVals = []
                for x, y in self.playersAndPositions[player.hero.name]:
                    xVals.append(x)
                    yVals.append(y)
                #im = pl.imread("dota_map.jpg")
                #imgplot = pl.imshow(im)
                #imgplot.set_interpolation('bicubic')
                pl.scatter(xVals, yVals)
                #pl.axis('image')
                pl.show()
                
                    
    
    def playerMovementScaleGraph(self, hero_name):
        for player in self.replay.players:
            if player.hero == hero_name:
                distance_data = []
                tick_data = []
                prevX, prevY = 0, 0
                self.replay.go_to_tick("game")
                currX, currY = player.hero.position
                #might have to change step size to get a better estimation of movement
                for tick in self.replay.iter_ticks(start="game", end="postgame", step=300):
                    if not player.hero.is_alive:
                        currX, currY = 0, 0
                        break
                    prevX, prevY = currX, currY
                    currX, currY = player.hero.position
                    dist_traveled = manhattan(currX, currY, prevX, prevY)
                    distance_data.append(dist_traveled)
                    tick_data.append(tick)
                #call plotting function
                plt.plot(tick_data, distance_data)
                plt.show()
                #plt.savefig("./playerMovementGraph.png")

    def itemsPurchased(self):
        for player in self.replay.players:
            for item in player.hero.inventory:
                self.itemList.append((item, item.purchase_time))
        
        #Bug testing
        #for item in self.itemList:
            #print(item)

    def netGold(self, hero_name):
        for player in self.replay.players:
            if player.hero == hero_name:
               return

    def goldPerMinute(self, hero_name):
        for player in self.replay.players:
            if player.hero == hero_name:


    def courierMovement(self, side):
        courierLocations = []
        for courier in self.replay.creeps.couriers:
            if courier.team == side:                       
                for tick in self.replay.iter_ticks(start="game", end="postgame"):
                    if not courier.is_alive:
                        break
                    courierLocations.append(courier.position)
                xVals = []
                yVals = []
                for x, y in courierLocations:
                    xVals.append(x)
                    yVals.append(y)
                #im = pl.imread("dota_map.jpg")
                #imgplot = pl.imshow(im)
                #imgplot.set_interpolation('bicubic')
                pl.scatter(xVals, yVals)
                #pl.axis('image')
                pl.show()
    
    def supportGoldHero(self, hero_name):
        for player in self.replay.players:
            if player.hero == hero_name:
                
                totalGold = 0
                current_items = []
                old_items = []

                for tick in self.replay.iter_ticks(start="game", end="postgame"):
                    old_items = current_items
                    current_items = []
                    
                    for item in player.hero.inventory:
                        current_items.append(item)
                    
                    for new_item in current_items:
                        for old_item in old_items:
                            if new_item == old_item:
                                break
                            else:
                                if new_item in self.supportItems:
                                    totalGold += self.supportItems[new_item]
                return totalGold


    def supportGoldTotal(self, side):


def manhattan(currX, currY, prevX, prevY):
    distance = math.sqrt(abs((currX - prevX) ** 2) + abs((currY - prevY) ** 2))
    return distance


"""class Heatmap:
    def __init__(self, x, y):
        self.x = x #An array of tuples of locations
        self.y = y

    def plot(self):
        #pl.subplot(121)
        pl.hexbin(self.x, self.y)
        pl.axis('image')
        pl.show()"""

def test():
    replayClass = Replay()    
    replaClass.initPlayersAndPositions()
    for player in replayClass.playersAndPositions:
        replayClass.playerMovementMap(player)
        break
    #replayClass.courierMovement("radiant")
    #replayClass.playerMovementGraph(heroNames[0])

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
