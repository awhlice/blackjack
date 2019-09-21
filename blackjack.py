import sys
import time
import random

class Player:
	def __init__(self, hand):
		self.hand = hand
	def points(self):
		points = 0
		for card in self.hand:
			if card.value == "Jack" or card.value == "Queen" or card.value == "King":
				points += 10
			elif card.value == "Ace":
				if points < 11: 
					points += 11
				else: 
					points += 1
			else: 
				points += card.value
		return points

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	def reveal(self):
		card = "{} of {}".format(self.value, self.suit)
		return card

class Deck:
	def __init__(self):
		self.cards = []
		self.create()
	def create(self):
		for value in range(1, 15):
			for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
				if value == 11: value = "Jack"
				if value == 12: value = "Queen"
				if value == 13: value = "King"
				if value == 14: value = "Ace"
				self.cards.append(Card(value, suit))
		random.shuffle(self.cards)

deck = Deck()

def deal():
	hand = []
	for i in range(2):
		card = deck.cards.pop()
		hand.append(card)
	return hand	

def begin(player, dealer):
	print_slowly("Let's play Blackjack!\n")
	print "-------------------------------------------------------------------------------------"
	print_slowly("You are holding the {} and {} for a total of {} points.\n".format(player.hand[0].reveal(), player.hand[1].reveal(), player.points()))
	print_slowly("The dealer is showing the {}.\n".format(dealer.hand[0].reveal()))
	if player.points() == 21:
		print_slowly("\nThe dealer checked their face-down card, and it is the {}.\n".format(dealer.hand[1].reveal()))
		if dealer.points() == 21:
			print_slowly("\nWho would've thought! The dealer also has Blackjack. You tied with the dealer.\n")
			print "-------------------------------------------------------------------------------------"
		else:
			print_slowly("\nWow, right off the bat! Congratulations, you got Blackjack!\n")
			print "-------------------------------------------------------------------------------------"
		print_slowly("Exiting Blackjack...\n")
		exit()
	elif dealer.points() == 21 and (dealer.hand[0].value == 10 or dealer.hand[0].value == "Ace"):
		print_slowly("\nThe dealer revealed their face-down card to be the {}.\n".format(dealer.hand[1].reveal()))
		print_slowly("\nHow unlucky! Sorry, you lose. The dealer got Blackjack.\n")
		print "-------------------------------------------------------------------------------------"
		print_slowly("Exiting Blackjack...\n")
		exit()

def hit(player, dealer):
	card = deck.cards.pop()
	if player: 
		player.hand.append(card)
		print_slowly("You received a {}. You now have a total of {} points.\n".format(player.hand[len(player.hand) - 1].reveal(), player.points()))
		if player.points() > 21:
			print_slowly("\nSorry, you lose! You busted.\n")
			print "-------------------------------------------------------------------------------------"
			print_slowly("Exiting Blackjack...\n")
			exit()
	elif dealer:
		dealer.hand.append(card)
		print_slowly("The dealer took the {}.\n".format(dealer.hand[len(dealer.hand) - 1].reveal()))

def stand(player, dealer):
	print_slowly("\nThe dealer revealed their face-down card to be the {}.\n".format(dealer.hand[1].reveal()))
	while dealer.points() < 17:
		hit(None, dealer)
	outcome(player, dealer)
	print "-------------------------------------------------------------------------------------"
	print_slowly("Exiting Blackjack...\n")
	exit()

def quit():
	print_slowly("Sad to see you go. Bye!\n")
	print "-------------------------------------------------------------------------------------"
	print_slowly("Exiting Blackjack...\n")
	exit()

def reveal_hands(player, dealer):
	print_slowly("\nTo recap, you are holding the ")
	for i in range(len(player.hand) - 1):
		if i == len(player.hand) - 2: 
			print_slowly(player.hand[i].reveal())
		else:
			print_slowly(player.hand[i].reveal() + ", ")
	print_slowly(" and {} for a total of {} points.\n".format(player.hand[len(player.hand) - 1].reveal(), player.points()))
	print_slowly("The dealer is holding the ")
	for i in range(len(dealer.hand) - 1):
		if i == len(dealer.hand) - 2: 
			print_slowly(dealer.hand[i].reveal())
		else:
			print_slowly(dealer.hand[i].reveal() + ", ") 
	print_slowly(" and {} for a total of {} points.\n".format(dealer.hand[len(dealer.hand) - 1].reveal(), dealer.points()))

def outcome(player, dealer):
	reveal_hands(player, dealer)
	if player.points() == dealer.points():
		print_slowly("\nWho would've thought! You tied with the dealer.\n")
	elif player.points() == 21:
		print_slowly("\nCongratulations, you got Blackjack!\n")
	elif dealer.points() == 21:
		print_slowly("\nSorry, you lose! The dealer got Blackjack.\n")
	elif player.points() > 21:
		print_slowly("\nSorry, you lose! You busted.\n")
	elif dealer.points() > 21:		   
		print_slowly("\nCongratulations, you win! The dealer busted.\n")
	elif player.points() > dealer.points():
		print_slowly("\nCongratulations, you win! Your hand is closer to 21 than the dealer.\n")
	elif player.points() < dealer.points():
		print_slowly("\nSorry, you lose! The dealer's hand is closer to 21.\n")

def print_slowly(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25)

def play():
	dealer = Player(deal())
	player = Player(deal())
	begin(player, dealer)
	while True:
		print_slowly("\nWould you like to [H]it, [S]tand, or [Q]uit? ")
		choice = raw_input().upper()
		if choice == 'H':
			hit(player, None)
		elif choice =='S':
			stand(player, dealer)
		elif choice == 'Q':
			quit()
		else:
			print_slowly("Sorry, you can't perform that action.\n")

if __name__ == "__main__":
	play()
