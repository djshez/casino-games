from blackjackTable import Deck, Hand
from Casino import Player
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
	#for item in range(len(d.cards)):
		#print(d[item], "item=", item)
	h = Hand()
	h.hit(d[2])
	h.hit(d[3])
	if h.getHandValue() != 4:
		return False
	h.hit(d[-1])
	if h.getHandValue() != 15:
		return False
	h.hit(d[36])
	print(h.getHandValue())
	return h.getHandValue() == 15

print(calculateHandValue())
