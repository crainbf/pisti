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
    while Card_Deck[discard_pile[-1]]['value'] == 'J':
        discard_pile = random.sample(deck, 4)
    deck = [x for x in deck if x not in discard_pile]

    # Create empty piles for the players
    player1_pile = []
    player2_pile = []

    return(deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile)


def arbitrate(player, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile, player1_pisti, player2_pisti, last_capture):
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
        return result, player_card, discard_pile, player1_pisti, player2_pisti, last_capture

    # The player pairs with the top card of the pile and takes pile
    if Card_Deck[player_card]['value'] == top_card_value:
        result = 1
        discard_pile.extend([player_card])
        # Cards get added to player1's pile
        if player == 1:
            player1_pile.extend(discard_pile)
            last_capture = 1
            # Check for Double Pisti
            if len(discard_pile) == 2 and Card_Deck[discard_pile[-1]]['value'] == "J":
                player1_pisti += 2
            # Check for Pisti
            elif len(discard_pile) == 2:
                player1_pisti += 1
        # Or to player2's pile
        else:
            player2_pile.extend(discard_pile)
            last_capture = 2
            # Check for Pisti
            if len(discard_pile) == 2 and Card_Deck[discard_pile[-1]]['value'] == "J":
                player2_pisti += 2
            # Check for Pisti
            elif len(discard_pile) == 2:
                player2_pisti += 1
        discard_pile = []
    # The player plays a jack and the discard pile is not empty the player takes the pile
    elif Card_Deck[player_card]['value'] == "J" and discard_pile:
        result = 1
        discard_pile.extend([player_card])
        # Cards get added to player1's pile
        if player == 1:
            player1_pile.extend(discard_pile)
            last_capture = 1
        # Or to player2's pile
        else:
            player2_pile.extend(discard_pile)
            last_capture = 2
        discard_pile = []
    # The player doesn't take the pile and the round continues
    else:
        result = 0
        discard_pile.extend([player_card])
    return result, player_card, discard_pile, player1_pisti, player2_pisti, last_capture


def deal(player1_hand, player2_hand, deck):
    # Draw four cards for player1's hand and remove them from the deck
    player1_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player1_hand]

    # Draw four cards for player2's hand and remove them from the deck
    player2_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in player2_hand]

    return player1_hand, player2_hand, deck


def score(player1_pile, player2_pile, player1_pisti, player2_pisti):
    # Here I will need to do the scoring algorithm
    player1_scores = []
    player2_scores = []

    # Add one point for each Ace and Jack
    player1_scores.extend([1 for i in player1_pile if (Card_Deck[i]['value'] == "J" or Card_Deck[i]['value'] == "A")])
    player2_scores.extend([1 for i in player2_pile if (Card_Deck[i]['value'] == "J" or Card_Deck[i]['value'] == "A")])

    # Add two points for the 2 of Clubs (Card Code 13)
    if 13 in player1_pile:
        player1_scores.extend([2])
    else:
        player2_scores.extend([2])

    # Add three points for the 10 of Diamonds
    if 34 in player1_pile:
        player1_scores.extend([3])
    else:
        player2_scores.extend([3])

    # Add three points for the card majority
    if len(player1_pile) > len(player2_pile):
        player1_scores.extend([3])
    elif len(player2_pile) > len(player1_pile):
        player2_scores.extend([3])

    # Add points for the Pistis
    player1_scores.extend([10*player1_pisti])
    player2_scores.extend([10*player2_pisti])

    # Calculate the total scores
    player1_score = sum(player1_scores)
    player2_score = sum(player2_scores)

    return player1_score, player2_score


def game():
    # Set up game with initial variables
    deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile = setup()
    last_capture = 0
    # Set initial pisti count to 0
    player1_pisti = player2_pisti = 0

    for i in range(48):
        # Determine player
        player = 1 if (i % 2 == 0) else 2
        print("Discard Pile :")
        try:
            top_discard_card = Card_Deck[discard_pile[-1]]['value']+" of "+Card_Deck[discard_pile[-1]]['suit']
        except IndexError:
            top_discard_card = "empty"
        print("Top Card :"+top_discard_card)
        print(discard_pile)
        print("Turn: "+str(i+1))
        try:
            result, player_card, discard_pile, player1_pisti, player2_pisti, last_capture = arbitrate(player, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile, player1_pisti, player2_pisti, last_capture)
        except IndexError:  # The player's hands have run out of cards and .pop returns and IndexError
            player1_hand, player2_hand, deck = deal(player1_hand, player2_hand, deck)
            result, player_card, discard_pile, player1_pisti, player2_pisti, last_capture = arbitrate(player, discard_pile, player1_hand, player2_hand, player1_pile, player2_pile, player1_pisti, player2_pisti, last_capture)
        print("Player "+str(player)+" plays "+Card_Deck[player_card]['value']+" of "+Card_Deck[player_card]['suit'])
        print("Deck Length: "+str(len(deck)))
        print("P1 Hand: "+str(player1_hand))
        print("P2 Hand: "+str(player2_hand))
        print("P1 Pistis: "+str(player1_pisti))
        print("P2 Pistis: "+str(player2_pisti))
        print("P1 Pile: "+str(player1_pile))
        print("P2 Pile: "+str(player2_pile))
        print(" ")

    if last_capture == 1:
        player1_pile.extend(discard_pile)
    else:
        player2_pile.extend(discard_pile)
    discard_pile = []  # Unnecessary. I can remove this later
    player1_score, player2_score = score(player1_pile, player2_pile, player1_pisti, player2_pisti)

    print("Player 1 scored: "+str(player1_score))
    print("Player 2 scored: "+str(player2_score))
    return deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile, player1_pisti, player2_pisti


# This is a test functions that checks for the length
def lengthy(deck, player1_hand, player2_hand, discard_pile, player1_pile, player2_pile, player1_pisti, player2_pisti):
    print("Deck length: "+str(len(deck)))
    print("P1 Hand: "+str(len(player1_hand)))
    print("P2 Hand: "+str(len(player2_hand)))
    print("Discard Pile: "+str(len(discard_pile)))
    print("P1 Pile: "+str(len(player1_pile)))
    print("P1 Pistis: "+str(player1_pisti))
    print("P2 Pistis: "+str(player2_pisti))
    print("P2 Pile: "+str(len(player2_pile)))
    print("Total cards: "+str(len(deck)+len(player1_hand)+len(player2_hand)+len(discard_pile)+len(player1_pile)+len(player2_pile)))

