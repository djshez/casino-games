from blackjackTable import Card, Deck, Hand
from collections import defaultdict, Counter

payouts = {'royalFlush':100,
			'straightFlush':50,
			'4ofakind':20,
			'fullHouse':15,
			'flush':10,
			'straight':8,
			'3ofakind':5,
			'2pair':2,
			'pair':1}

class pokerDeck(Deck):
	suits = 'spades diamonds clubs hearts'.split()
	ranks = [str(num) for num in range(2,11)] + list('JQKA')
	values = dict(zip(ranks, [x for x in range(2,15)]))
	
class pokerHand(Hand):
	
	def delete(self, cardIndices):
		for index in sorted(cardIndices, reverse=True):
			del self.contents[index]
			
	def payout(self):
		'''Uses default dictionaries to determine what and how many
		of each card the player has. Then does a check to determine
		the correct payout.
		'''
		suits = defaultdict(int)
		ranks = defaultdict(int)
		straightCheck = []
		for card in self.contents:
			suits[card.suit] += 1
			ranks[card.rank] += 1
			straightCheck.append(card.value)
		twoPairCheck = Counter(ranks.values())
		
		if (5 in suits.values() and
			'A' in ranks and
			'K' in ranks and
			'Q' in ranks and
			'J' in ranks and
			'10' in ranks):
			print("WOW! Royal Flush!")
			return payouts['royalFlush']
		elif 5 in suits.values() and sorted(straightCheck) == [x for x in range(min(straightCheck), max(straightCheck)+1)]:
			print("You have a Straight Flush! Nice!")
			return payouts['straightFlush']
		elif 4 in ranks.values():
			print("You have Four of a Kind!")
			return payouts['4ofakind']
		elif 3 in ranks.values() and 2 in ranks.values():
			print('You have a Full House!')
			return payouts['fullHouse']
		elif 5 in suits.values():
			print('You have a Flush!')
			return payouts['flush']
		elif sorted(straightCheck) == [x for x in range(min(straightCheck), max(straightCheck)+1)]:
			print('You have a Straight!')
			return payouts['straight']
		elif 3 in ranks.values():
			print("You have a 3 of a kind!")
			return payouts['3ofakind']
		elif twoPairCheck[2] == 2:
			print("You have 2 pair!")
			return payouts['2pair']
		elif 2 in ranks.values():
			print("You have a pair!")
			return payouts['pair']
		else:
			print("Sorry you don't have anything")
			return 0
	
def main(player):
	print("\nWelcome to Video Poker, {}.".format(player.getName()))
	deck = pokerDeck()
	
	while True:
		print("Your current bankroll = $", player.getBankroll())
		bet = int(input("Please make a wager- $"))
		player.decreaseBankroll(bet)
		deck.shuffle()
		hand = pokerHand()
		for num in range(5):
			hand.hit(deck.dealCard())
		print("Your cards:\n", hand)
		
		indicesToRemove = []
		print("""Which card(s) would you like to replace?
		(Enter card numbers(1-5))
		Enter blank line when finished""")
		while True:
			index = input()
			if index:
				try:
					index = int(index) - 1
				except ValueError:
					print("Must be a number (1-5)")
					continue
				indicesToRemove.append(index)
			else:
				break
		
		if indicesToRemove:
			hand.delete(indicesToRemove)
			for num in range(len(indicesToRemove)):
				hand.hit(deck.dealCard())
		print("Your new cards:\n", hand)
		multiplier = hand.payout()
		print("You won - $" + str(bet*multiplier))
		player.increaseBankroll(bet*multiplier)
		
		keepPlaying = input("Do you want to keep playing? (y or n) ")
		if keepPlaying.lower() == 'n':
			break
	
	print("Thanks for playing. Come again!")
	
if __name__ == '__main__':
	print("Please run Casino.py")