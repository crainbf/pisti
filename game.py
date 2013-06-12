import random
from deck import Card_Deck
# from arbitrate import arbitrate

# Create a card array
deck = range(52)
# Shuffle cards
random.shuffle(deck)


# Note: We will need to make sure that cards are not drawn with replacement
# Create random player hands of four cards each
player1_hand = random.sample(deck, 4)

# Remove player1_hand from deck
deck = [x for x in deck if x not in player1_hand]

# Draw player2_hand
player2_hand = random.sample(deck, 4)

# Remove player2_hand from deck
deck = [x for x in deck if x not in player2_hand]

# Create a discard pile 
discard_pile = random.sample(deck, 4)

# Remove discard pile from deck
deck = [x for x in deck if x not in discard_pile]

# Creating empty piles for the players
player1_pile = []
player2_pile = []


def arbitrate(player1_card, player2_card, discard_pile):
    # This function chooses the winning hand
    # if the value of player2_card is equal to that of player 1-> he wins
    # else 'The pile is getting higher'
    player1_cvalue = Card_Deck[player1_card]['value']
    player2_cvalue = Card_Deck[player2_card]['value']

    # player2's card has the same value as player 1's card
    if player1_cvalue == player2_cvalue:
        result = "Player 2 wins the hand by pairing"
        player2_pile.extend([player1_card, player2_card])
        discard_pile = []

    # player2 plays a jack
    elif player2_cvalue == 'J':
        result = "Player 2 wins the hand by playing a Jack"
        player2_pile.extend([player1_card, player2_card])
        discard_pile = []

    else:
        result = "Next round"
        # THIS IS WRONG. JUST TO TEST. CORRECT!
        discard_pile.extend([player1_card, player2_card])

    return result, discard_pile

# Player 1 begins the game
# 1. player 1 appends a card to the discard pile
# 2. function arbitrate checks
#    - if the last two cards on the discard pile are identical
#    - or if the last card on the discard pile is a 'J'
#  if TRUE:
#      - the discard pile is appended to p1_pile
#      - the discard pile is emptied
#      - it returns to 1.
# if FALSE:
#      - player2 appends a card to the discount pile
#
#
# necessary functions:
#    check if last two are identical


for i in range(4):
    result, discard_pile = arbitrate(player1_hand[i], player2_hand[i], discard_pile)
    print(result, discard_pile)

# game
# first cards for each player is saved in variable
# cards are passed to arbitration function
# arbitration function returns outcome (e.g. string 'the winner is 1 or 2')


# print(player1_hand, player2_hand, discard_pile)

# for i in range(4):
#     print("Hand: %s" %i)
#     print("Player 1's play: %s of %s" % (Card_Deck[player1_hand[i]]['value'], Card_Deck[player1_hand[i]]['suit']))
