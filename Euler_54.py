"""
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:
	Hand             Player 1          Hand              Player 2           Winner
5H 5C 6S 7S KD => Pair of Fives    | 2C 3S 8S 8D TD => Pair of Eights     ==> Player 2
5D 8C 9S JS AC => Highest card Ace | 2C 5C 7D 8S QH => Highest card Queen ==> Player 1
2D 9C AS AH AC => Three Aces       | 3D 6D 7D TD QD => Flush with Diamonds => Player 2
4D 6S 9H QH QC => Pair of Queens Highest card Nine | 3D 6D 7H QD QS Pair of Queens Highest card Seven Player 1
2H 2D 4C 4D 4S => Full House With Three Fours | 3C 3D 3S 9S 9D Full House with Three Threes           Player 1
The file "resources/documents/0054_poker.txt", contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""
import os


ROOT_DIR = os.getcwd()
with open(ROOT_DIR + '/data/Euler_54') as f:
	lines = f.readlines()
	player_1_wins = 0
	for line in lines:
		line = line[:-1].split(sep=' ')
		
		player_1_cards = line[:5]
		player_2_cards = line[5:]
		
		def make_comb(hand: list) -> tuple:
			suits_amount = len(set([card[1] for card in hand]))  # suits
			flash = False
			if suits_amount == 1:
				flash = True
			cards_values = [card[0] for card in hand]  # values
			v_dict: dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
			values = []
			for v in cards_values:
				if v.isdigit():
					values.append(int(v))
				elif v in v_dict:
					values.append(v_dict[v])
				else:
					raise Exception(f'Unknown hand {hand} card {v}')
			sorted_cards = sorted(values)
			if flash:
				return sorted_cards, 'flash'
			have_straight = None
			for n in range(4):
				if sorted_cards[n] + 1 != sorted_cards[n + 1]:
					break
			else:  # Full cycle
				if flash:  # STRAIGHT FLASH
					return sorted_cards, 'straight flash'
				else:
					have_straight = sorted_cards, 'straight'
			hand_dict: dict = {}
			for v in sorted_cards:
				if v not in hand_dict:
					hand_dict[v] = 1
				else:
					hand_dict[v] = hand_dict[v] + 1
			values = [hand_dict[v] for v in hand_dict]
			high_same = max(values)
			if high_same == 4:
				quads_value = None
				for v in hand_dict:
					if hand_dict[v] == 4:
						quads_value = v
					else:
						return (quads_value, v), 'quads'
			elif high_same == 3:  # Full-house or trips
				triplet_value = None
				duplet_value = None
				for v in hand_dict:
					if hand_dict[v] == 3:
						triplet_value = v
					elif hand_dict[v] == 2:
						duplet_value = v
				else:
					if triplet_value is not None and duplet_value is not None:
						return (triplet_value, duplet_value), 'full-house'
					# elif flash:  # Have flash
					# 	return sorted_cards, 'flash'
					elif have_straight:  # Have straight
						return have_straight
					else:  # Trips and kicker
						return (triplet_value, sorted([hand_dict[v] for v in hand_dict if v != triplet_value])), 'trips'
			elif high_same == 2:  # Two pairs or pair
				higher_pair_v = None
				lower_pair_v = None
				for v in hand_dict:
					if hand_dict[v] == 2:
						if higher_pair_v is None and lower_pair_v is None:
							lower_pair_v = v
						else:  # lower pair not None
							if v > lower_pair_v:
								higher_pair_v = v
							else:
								higher_pair_v = lower_pair_v
								lower_pair_v = v
				if higher_pair_v is None:  # One pair
					return (lower_pair_v, sorted([v for v in hand_dict if v != lower_pair_v])), 'pair'
				else:  # Two pairs
					return (higher_pair_v, lower_pair_v,
					        [v for v in hand_dict if v != lower_pair_v and v != higher_pair_v][0]), 'two pairs'
			elif have_straight:
				return have_straight
			else:  # High cards
				return sorted_cards, 'high card'
		
		info1, comb_1 = make_comb(player_1_cards)
		info2, comb_2 = make_comb(player_2_cards)
		
		all_combs = ('high card', 'pair', 'two pairs', 'trips', 'straight', 'flash', 'full-house', 'quads', 'straight-flash')
		try:
			player_1_combo_strength = all_combs.index(comb_1)
			player_2_combo_strength = all_combs.index(comb_2)
		except ValueError:
			print(comb_1, comb_2)
		if player_1_combo_strength > player_2_combo_strength:
			player_1_wins += 1
		elif player_1_combo_strength == player_2_combo_strength:
			def compare_sorted(s1: list, s2: list):
				for index, v in enumerate(s1[::-1]):
					if v > s2[-index-1]:
						return True
					elif v < s2[-index-1]:
						return False
				else:
					raise Exception('Split')
			
			if comb_1 == 'high card':
				if compare_sorted(s1=info1, s2=info2):
					player_1_wins += 1
			elif comb_1 == 'pair':
				p1 = info1[0]
				p2 = info2[0]
				if p1 > p2:
					player_1_wins += 1
				elif p1 == p2:
					if compare_sorted(s1=info1[1], s2=info2[1]):
						player_1_wins += 1
			elif comb_1 == 'two pairs':
				tp1 = info1[0]
				tp2 = info2[0]
				if tp1 > tp2:
					player_1_wins += 1
				elif tp1 == tp2:
					lp1 = info1[1]
					lp2 = info2[1]
					if lp1 > lp2:
						player_1_wins += 1
					elif lp1 == lp2:
						if info1[2] > info2[2]:
							player_1_wins += 1
						elif info2[2] == info2[2]:
							raise Exception('Split')
			elif comb_1 == 'trips':
				t1 = info1[0]
				t2 = info2[0]
				if t1 > t2:
					player_1_wins += 1
				elif t1 == t2:
					if compare_sorted(s1=info1[1], s2=info2[1]):
						player_1_wins += 1
			elif comb_1 == 'straight':
				if compare_sorted(s1=info1, s2=info2):
					player_1_wins += 1
			elif comb_1 == 'flash':
				if compare_sorted(s1=info1, s2=info2):
					player_1_wins += 1
			elif comb_1 == 'full-house':
				tp1 = info1[0]
				tp2 = info2[0]
				if tp1 > tp2:
					player_1_wins += 1
				elif tp1 == tp2:
					dp1 = info1[1]
					dp2 = info2[1]
					if dp1 > dp2:
						player_1_wins += 1
			elif comb_1 == 'quads':
				q1 = info1[0]
				q2 = info2[0]
				if q1 > q2:
					player_1_wins += 1
				elif q1 == q2:
					if info1[1] > info2[1]:
						player_1_wins += 1
					elif info2[1] == info2[1]:
						raise Exception('Split')
			elif comb_1 == 'straight-flash':
				if compare_sorted(s1=info1, s2=info2):
					player_1_wins += 1
	print(player_1_wins)
