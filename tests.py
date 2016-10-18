from Blackjack import Player, Deck, Hand

#Test Player Class
def addMoneyToPlayer():
	p1 = Player(1000)
	p1.increaseBankroll(50)
	return p1.bankroll == 1050
def removeMoneyFromPlayer():
	p1 = Player(1000)
	p1.decreaseBankroll(50)
	return p1.bankroll == 950

#Test Deck Class
def shuffle():
	d = Deck()
	o = Deck()
	o.shuffle()
	return d != o
def cardNotPresentAfterDeal():
	d = Deck()
	d.shuffle()
	target = d.dealCard()
	return target not in d.cards

#Test Hand Class
def addToHand():
	d = Deck()
	h = Hand()
	h.hit(d.dealCard())
	return len(h) > 0
def calculateHandValue():
	d = Deck()
	h = Hand()
	h.hit(d[-1])
	h.hit(d[13])
	if h.getHandValue() != 16:
		return False
	h.hit(d[26])
	if h.getHandValue() != 14:
		return False
	h.hit(d[19])
	return h.getHandValue() == 20

