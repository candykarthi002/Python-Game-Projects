import random


kinds = ["Hearts", "Spades", "Clovers", "Diamond"]
ranks = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card:
	def __init__(self, kind, rank):
		self.kind = kind
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.kind}."


class Deck:
	def __init__(self):
		self.cards = self.generate_deck()

	def generate_deck(self):
		deck = []
		for kind in kinds:
			for rank in ranks:
				card = Card(kind, rank)
				deck.append(card)
		return deck

	def shuffle(self):
		random.shuffle(self.cards)

class Player:
	def __init__(self, name, deck):
		self.name = name
		self.deck = deck

	def draw_one(self):
		return self.deck.pop(0)

	def add_cards(self, cards):
		if type(cards) == type([]):
			self.deck.extend(cards)
		else:
			self.deck.append(cards)

	def __str__(self):
		return f"{self.name} has {len(self.deck)} cards."

base_deck = Deck()
# print(base_deck.cards)

base_deck.shuffle()
# print(base_deck.cards)

first_half_cards = base_deck.cards[:len(base_deck.cards)//2]
last_half_cards = base_deck.cards[len(base_deck.cards)//2:]

player1 = Player("Karthik", first_half_cards)
player2 = Player("Akash", last_half_cards)

print(player1)
# for card in player1.deck:
# 	print(card)

print(player2)
# for card in player2.deck:
# 	print(card)

p1_card = ranks[player1.draw_one().rank]
p2_card = ranks[player2.draw_one().rank]

print(p1_card)
print(p2_card)

print(player1)
print(player2)

print("Player1" if p1_card > p2_card else "Player2")