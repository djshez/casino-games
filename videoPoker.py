from blackjackTable import Card, Deck, Hand


		
	
	
	
def main(player):
	print("\nWelcome to Video Poker, {}.".format(player.getName()))
	deck = Deck()
	
	while True:
		bet = input("Please make a wager- $")
		deck.shuffle()
		hand = pokerHand()
		for num in range(5):
			hand.hit(deck.dealCard())
		print("Your cards:\n", hand)
		draw = input("Which card(s) would you like to replace? ")
		
		#delete those cards from hand
		
		for num in range(len(draw)):
			hand.hit(deck.dealCard())
			
		#check what the player has
		#display what they have and payout
		
		keepPlaying = input("Do you want to keep playing? (y or n) ")
		if keepPlaying.lower() == 'n':
			break
	
	print("Thanks for playing. Come again!")
	

if __name__ == '__main__':
	print("Please run Casino.py")