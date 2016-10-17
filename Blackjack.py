from random import choice, shuffle

class Card(object):
	
	def __init__(self, rank, suit, value):
		self.rank = rank
		self.suit = suit
		self.value = value
	
	def __str__(self):
		return '{} of {}'.format(self.rank, self.suit)

class Deck(object):
	'''
	A deck made of 52 cards.
	'''
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
		shuffle(self.cards)
		
	def dealCard(self):
		return self.cards.pop(0)
		
class Hand(object):
	
	def __init__(self):
		self.contents = []
	
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


d = Deck()
d.shuffle()
p1 = Hand()


p1.hit(d.dealCard())
p1.hit(d.dealCard())
print(p1)
print(p1.getHandValue())
print(len(d))

p1.hit(d.dealCard())
print(p1)
print(p1.getHandValue())
print(len(d))

p1.hit(d.dealCard())
print(p1)
print(p1.getHandValue())
print(len(d))