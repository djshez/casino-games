import blackjackTable

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

def getHighScore():
	try:
		f = open('highscore.txt', 'r')
	except:
		return "No high score yet."
	highScore = f.read().split(':')
	f.close()
	return "Current High Score = " + highScore[0] + " - $" + highScore[1]

def updateHighScore(name, highScore):
        '''Check if new score is better than old high
        score and update the results.'''
        try:
                f = open('highscore.txt', 'r+')
                oldHighScore = f.read().split(':')
                if int(oldHighScore[1]) < highScore:
                        f.seek(0)
                        f.write(name+":"+str(highScore))
                        f.close()
                else:
                        f.close()
        except IOError:
                f = open('highscore.txt', 'w+')
                f.write(name+":"+str(highScore))
                f.close()

def setDifficulty(difficulty, name):
	if difficulty.lower() == 'novice' or difficulty == '3000':
		return Player(name, 3000)
	elif difficulty.lower() == 'weekend gambler' or difficulty == '2000':
		return Player(name, 2000)
	elif difficulty.lower() == 'pro' or difficulty == '1000':
		return Player(name, 1000)

def main():
	print("Welcome to the casino! May the odds be ever in your favor.")
	name = input("What is your name?")
	difficulty = input("What type of gambler are you? Novice($3000), Weekend Gambler ($2000), Pro ($1000)? ")
	player = setDifficulty(difficulty, name)
	
	while True:
		mainChoice = input('''Now, what would you like to do?/n
						Check high score = 1/n
						Check current bankroll = 2/n
						Play Blackjack = 3/n
						Go home = 4/n''')
		if mainChoice == '1':
			print(getHighScore())
		elif mainChoice == '2':
			print("Your current bankroll = $" + player.getBankroll())
		elif mainChoice == '3':
			blackjackTable.main(player)
		elif mainChoice == '4':	
			updateHighScore(player.getName(), player.getBankroll())
			break
		else:
			print(mainChoice, "wasn't one of your options")
			continue
	
	print("Thank you for playing and come again soon!")
	
if __name__ == '__main__':	
	main()