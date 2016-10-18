from random import choice, shuffle

class Card(object):
	
	def __init__(self, rank, suit, value):
		self.rank = rank
		self.suit = suit
		self.value = value
	
	def __str__(self):
		return '{} of {}'.format(self.rank, self.suit)

class Deck(object):
	#A deck made of 52 cards.
	suits = 'spades diamonds clubs hearts'.split()
	ranks = [str(num) for num in range(2,11)] + list('JQKA')
	values = dict(zip(ranks, [x for x in range(2,11)] + [10,10,10, (1,11)]))
	
	def __init__(self):
		self.cards = [Card(rank, suit, self.values[rank]) for rank in self.ranks
										for suit in self.suits]
	def __getitem__(self, index):
		return self.cards[index]
	
	def __len__(self):
		return len(self.cards)
	
	def shuffle(self):
		#Pick up (reset) the cards and reshuffle.
		self.cards = [Card(rank, suit, self.values[rank]) for rank in self.ranks
										for suit in self.suits]
		shuffle(self.cards)
		
	def dealCard(self):
		return self.cards.pop(0)
		
class Hand(object):
	
	def __init__(self):
		self.contents = []
	
	def __len__(self):
		return len(self.contents)
	
	def __str__(self):
		return ', '.join([str(x) for x in self.contents])
	
	def hit(self, card):
		self.contents.append(card)

	def getHandValue(self):
		'''
		Sums the values of the cards in the hand.
		Does a check to assign either 11 or 1 to Ace.
		'''
		count = 0
		for card in sorted(self.contents, key=lambda card: card.rank):
			if card.rank == 'A':
				if count < 10:
					card.value = 11
				else:
					card.value = 1
			count += card.value
		return count
		
def main(player):
	print("\nWelcome to the Blackjack Table, {}.".format(player.getName()))
	while True:
		bet = float(input("Please place a bet: "))
		if bet > player.getBankroll():
			print("Current bankroll = {}. You don't have enough to cover that bet.".format(player.getBankroll()))
			continue
		player.decreaseBankroll(bet)
		deck = Deck()
		deck.shuffle()
		playerHand = Hand()
		playerHand.hit(deck.dealCard)
		playerHand.hit(deck.dealCard)
		dealerHand = Hand()
		dealerHand.hit(deck.dealCard)
		print("Dealer's up card - {}".format(dealerHand))
		dealerHand.hit(deck.dealCard)
		
		while True:
			print("Your cards- {}".format(playerHand))
			print("You have {}".format(playerHand.getHandValue()))
			playOrStay = input("Would you like to hit(h) or stay(s)? ")
			if playOrStay == 'h':
				playerHand.hit(deck.dealCard())
			elif playOrStay == 's':
				pass
			else:
				print("Not valid input. Type 'h' to hit or 's' to stay.")
				continue
			
		
		
		
	
	
	
	
	
	
	
