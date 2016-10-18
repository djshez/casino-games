import Blackjack

class Player(object):
	
	def __init__(self, name, bankroll=0):
		self.name = name
		self.bankroll = bankroll
	
	def __str__(self):
		return "{}'s bankroll = ${}".format(self.name, self.bankroll)
	
	def getName(self):
		return self.name
	
	def getBankroll(self):
		return self.bankroll
		
	def increaseBankroll(self, amount):
		self.bankroll += amount
		
	def decreaseBankroll(self, amount):
		self.bankroll -= amount