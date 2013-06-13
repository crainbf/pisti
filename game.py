import random
from deck import Card_Deck
# from arbitrate import arbitrate
# Create a card array
def setup():
    deck = range(52)
    # Shuffle cards
    random.shuffle(deck)

    # Draw player1's hand and remove it from the deck
    player1_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player1_hand]

    # Draw player2's hand and remove it from the deck
    player2_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player2_hand]

    # Draw the discard_pile and remove it from the deck
    discard_pile = random.sample(deck, 4)
    deck = [x for x in deck if x not in discard_pile]

    # Create empty piles for the players
    player1_pile = []
    player2_pile = []

    return(deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile)


def arbitrate(player, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile):
    if player == 1:
        player_card = player1_hand.pop()
    else:
        player_card = player2_hand.pop()

    try:
        top_card_value = Card_Deck[discard_pile[-1]]['value']
    # In case the discard pile is empty, the card is simply added to the pile
    except IndexError:
        result = 0
        discard_pile.extend([player_card])
        return result, player_card, discard_pile

    # The player pairs with the top card of the pile and takes pile
    if Card_Deck[player_card]['value'] == top_card_value:
        result = 1
        discard_pile.extend([player_card])
        # Cards get added to player1's pile
        if player == 1:
            player1_pile.extend(discard_pile)
        # Or to player2's pile
        else:
            player2_pile.extend(discard_pile)
        discard_pile = []
    # The player plays a jack and the discard pile is not empty the player takes the pile
    if Card_Deck[player_card]['value'] == "J" and not discard_pile:
        result = 1
        discard_pile.extend([player_card])
        # Cards get added to player1's pile
        if player == 1:
            player1_pile.extend(discard_pile)
        # Or to player2's pile
        else:
            player2_pile.extend(discard_pile)
        discard_pile = []
    # The player doesn't take the pile and the round continues
    else:
        result = 0
        discard_pile.extend([player_card])
    return result, player_card, discard_pile

def deal(player1_hand, player2_hand, deck):
    # Draw four cards for player1's hand and remove them from the deck
    player1_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player1_hand]

    # Draw four cards for player2's hand and remove them from the deck
    player2_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player2_hand]

    return player1_hand, player2_hand, deck

def score(player1_pile, player2_pile):
    # Here I will need to do the scoring algorithm
    player1_score = player2_score = 99

    return player1_score, player2_score

def game():
    # Set up game with initial variables
    deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile = setup()

    for i in range(26):
        # Player 1's turn
        print("Turn: "+str(2*i+1))
        try:
            r, p, d = arbitrate(1, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile)
        except IndexError:  # The player's hands have run out of cards and .pop returns and IndexError
            try:
                player1_hand, player2_hand, deck = deal(player1_hand, player2_hand, deck)
                r, p, d = arbitrate(1, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile)
            except ValueError:  # The deck has run out of cards and dealing returns a ValueError
                player1_score, player2_score = score(player1_pile, player2_pile)
        print("Player 1 plays "+Card_Deck[p]['value']+" of "+Card_Deck[p]['suit'])
        # Player 2's turn
        print("Turn: "+str(2*i+2))
        try:
            r, p, d = arbitrate(2, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile)
        except IndexError:  # The player's hands have run out of cards and .pop returns and IndexError
            try:
                player1_hand, player2_hand, deck = deal(player1_hand, player2_hand, deck)
                r, p, d = arbitrate(2, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile)
            except ValueError:  # The deck has run out of cards and dealing returns a ValueError
                player1_score, player2_score = score(player1_pile, player2_pile)
        print("Player 1 plays "+Card_Deck[p]['value']+" of "+Card_Deck[p]['suit'])
    return deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile


# This is a test functions that checks for the length
def lengthy(deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile):
    print("Deck length: "+str(len(deck)))
    print("P1 Hand: "+str(len(player1_hand)))
    print("P2 Hand: "+str(len(player2_hand)))
    print("Discard Pile: "+str(len(discard_pile)))
    print("P1 Pile: "+str(len(player1_pile)))
    print("P2 Pile: "+str(len(player2_pile)))
    print("Total cards: "+str(len(deck)+len(player1_hand)+len(player2_hand)+len(discard_pile)+len(player1_pile)+len(player2_pile)))

