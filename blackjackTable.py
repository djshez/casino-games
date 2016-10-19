from random import shuffle

class Card(object):
	
	def __init__(self, rank, suit, value, sort):
		self.rank = rank
		self.suit = suit
		self.value = value
		self.sort = sort
	
	def __str__(self):
		return '{} of {}'.format(self.rank, self.suit)

class Deck(object):
	#A deck made of 52 cards.
	suits = 'spades diamonds clubs hearts'.split()
	ranks = [str(num) for num in range(2,11)] + list('JQKA')
	values = dict(zip(ranks, [x for x in range(2,11)] + [10,10,10,11]))
	
	def __init__(self):
		self.cards = [Card(rank, suit, self.values[rank], self.values[rank]) for rank in self.ranks
										for suit in self.suits]
	def __getitem__(self, index):
		return self.cards[index]
	
	def __len__(self):
		return len(self.cards)
	
	def shuffle(self):
		#Pick up (reset) the cards and reshuffle.
		self.cards = [Card(rank, suit, self.values[rank], self.values[rank]) for rank in self.ranks
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
		for card in sorted(self.contents, key=lambda card: card.sort):
			if card.rank == 'A':
				if count <= 10:
					card.value = 11
				else:
					card.value = 1
			count += card.value
		return count

def checkIfOver(handTotal):
	return handTotal > 21

def checkIfBlackjack(handTotal):
	return handTotal == 21

def checkWhoWon(dealer, player):
	if dealer.getHandValue() > player.getHandValue():
		return dealer
	if dealer.getHandValue() == player.getHandValue():
		return None
	else:
		return player
	
def main(player):
	print("\nWelcome to the Blackjack Table, {}.".format(player.getName()))
	
	while True:
		loser = False
		print("Your bankroll = ${}".format(player.getBankroll()))
		bet = int(input("Please place a bet: "))
		if bet > player.getBankroll():
			print("Current bankroll = {}. You don't have enough to cover that bet.".format(player.getBankroll()))
			continue
		player.decreaseBankroll(bet)
		deck = Deck()
		deck.shuffle()
		playerHand = Hand()
		playerHand.hit(deck.dealCard())
		playerHand.hit(deck.dealCard())
		dealerHand = Hand()
		dealerHand.hit(deck.dealCard())
		print("Dealer's up card - {}".format(dealerHand))
		dealerHand.hit(deck.dealCard())
		
		#Check if either Player or Dealer has a Blackjack
		if checkIfBlackjack(playerHand.getHandValue()) and checkIfBlackjack(dealerHand.getHandValue()):
			print("Both player and dealer have Blackjack! Tie")
			continue
		elif checkIfBlackjack(playerHand.getHandValue()):
			print("Player has Blackjack! Player wins 3 to 2")
			player.increaseBankroll(bet*1.5)
		elif checkIfBlackjack(dealerHand.getHandValue()):
			print("I'm sorry Dealer has Blackjack. You lose.")
			continue
		
		#Player's turn
		while True:
			print("Your cards- {}".format(playerHand))
			print("You have {}".format(playerHand.getHandValue()))
			playOrStay = input("Would you like to hit(h) or stay(s)? ")
			if playOrStay == 'h':
				playerHand.hit(deck.dealCard())
				if checkIfOver(playerHand.getHandValue()):
					loser = True
					break
			elif playOrStay == 's':
				break
			else:
				print("Not valid input. Type 'h' to hit or 's' to stay.")
		
		while dealerHand.getHandValue() < 17:
			dealerHand.hit(deck.dealCard())
		
		#Determine the winner
		if loser:
			print("I'm sorry, you went over.")
		else:
			if checkIfOver(dealerHand.getHandValue()):
				print("Dealer broke. You win")
				player.increaseBankroll(bet*2)
			else:
				winner = checkWhoWon(dealerHand, playerHand)
				if winner == playerHand:
					print("Dealer's cards: {}".format(dealerHand))
					print("Your total = {}, dealer's total = {}. You win!".format(playerHand.getHandValue(),dealerHand.getHandValue()))
					player.increaseBankroll(bet*2)
				elif winner == None:
					print("Dealer's cards: {}".format(dealerHand))
					print("Your total = {}, dealer's total = {}. Tie!".format(playerHand.getHandValue(),dealerHand.getHandValue()))
					player.increaseBankroll(bet)
				else:
					print("Dealer's cards: {}".format(dealerHand))
					print("Your total = {}, dealer's total = {}. You lost :(".format(playerHand.getHandValue(),dealerHand.getHandValue()))
		keepPlaying = input("Would you like to keep playing? (y or n) ")
		
		if keepPlaying.lower() == 'n':
			break
		
	print("Thank you for playing. See you again soon!")

if __name__ == '__main__':
	print("Please run the Casino.py file")
	
	
	
	
