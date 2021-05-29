import random

# Trying to create a game of Mahjong to test python skills

# Data structure for the tiles
# 1-9 in 3 suits, man, sou, and pinzu. Plus 3 dragons and 4 winds. 4 of each tile
class tile:
	def __init__(self, suit, value, numid):
		self.suit = suit
		self.value = value
		self.string = self.value + ' ' + self.suit + ' '
		self.numid = numid

# Initialize a full tileset of 136 tiles
class deck:
	
	# Generate a tileset with a tileID unique to each tile
	def __init__(self):
		self.tileSet = []
		tileID = 0 
		for suit in ['man','sou','pinzu']:
			for value in ['1','2','3','4','5','6','7','8','9']:
				for i in range(4):
					newTile = tile(suit, value, tileID)
					tileID += 1 
					self.tileSet.append(newTile)
		for dragon in ['red','green','white']:
			for i in range(4):
				newTile = tile(dragon, '', tileID)
				tileID += 1 
				self.tileSet.append(newTile)
		for wind in ['east','south','west','north']:
			for i in range(4):
				newTile = tile(wind,'', tileID)
				tileID += 1 
				self.tileSet.append(newTile)

	def remaining(self):
		return (len(self.tileSet))

class player: 

	def __init__(self, seatWind, deck, name):
		self.hand = []
		self.discards = []
		self.seatWind = seatWind
		self.name = name
		self.deck = deck

		#Draw 13 tiles from the deck
		for i in range(13):
			tileDraw = random.choice(self.deck.tileSet)
			self.hand.append(tileDraw)
			self.deck.tileSet.remove(tileDraw)

		self.sortHand()

	def printhand(self):
		handString = ""
		for tile in self.hand:
			handString += tile.string
		return handString

	# Function for the class Player that sorts the hand by numerical value and suit. 

	def sortHand(self):
		newList = list(self.hand)
		newHand = []
		cache = []
		for suitOrder in ['man','pinzu','sou','red','east','west','south','west','north','red','white','green']:
			for tile in newList:
				if tile.suit == suitOrder:
					cache.append(tile)
			for i in range(1, 10):
				for tile in cache:
					if tile.value == str(i):
						newHand.append(tile)
						cache.remove(tile)
					elif tile.value == '':
						newHand.append(tile)
						cache.remove(tile)

		self.hand = newHand

class table:
	def __init__(self, num_players, deck, names = []):
		self.seats = []
		self.deck = deck
		self.num_players = num_players
		self.names = names

		self.winds = ['East','South','West','North']

		for i in range(num_players):
			seatTaker = player(self.winds[i], self.deck, self.names[i] )
			self.seats.append(seatTaker)

print("Hello, welcome to PyMJ.")

testDeck = deck()
testTable = table(4, testDeck, ['Patrick', 'David', 'Beth','Mimi'])
print(str(testDeck.remaining()) + " tiles remaining in the deck after initial draw.")
for player in testTable.seats:
	print(player.name)
	print(player.printhand())

