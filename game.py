import random
from deck import Card_Deck
import time


def deal_initial():
    # Sets up the game by shuffling cards and doing initial deal
    # RETURNS: Players' hands, deck, discard pile, players' piles

    """
    >>> deck, p1_hand, p2_hand, discard_pile, p1_pile, p2_pile = deal_initial()
    >>> len(deck)
    40
    >>> len(p1_hand) == len(p2_hand) == 4
    True
    >>> Card_Deck[discard_pile[-1]]['value'] != 'J'
    True
    """

    deck = range(52)
    # Shuffle cards
    random.shuffle(deck)

    # Draw player1's hand and remove it from the deck
    p1_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in p1_hand]

    # Draw player2's hand and remove it from the deck
    p2_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in p2_hand]

    # Draw the discard_pile and remove it from the deck
    discard_pile = random.sample(deck, 4)
    while Card_Deck[discard_pile[-1]]['value'] == 'J':
        discard_pile = random.sample(deck, 4)
    deck = [x for x in deck if x not in discard_pile]

    # Create empty piles for the players
    p1_pile = []
    p2_pile = []

    return deck, p1_hand, p2_hand, discard_pile, p1_pile, p2_pile


def choose_card(p2_hand):
    # Shows cards in player's hand and allows selection of playing card.
    # RETURNS: Card played, Player's hand

    print("You have the following cards:")
    for i in range(len(p2_hand)):
        print("Card " + str(i+1) + ': ' + Card_Deck[p2_hand[i]]['value'] + ' of ' + Card_Deck[p2_hand[i]]['suit'] + '.')
    card_choice = 0
    while int(card_choice) not in range(1, len(p2_hand) + 1):
        card_choice = raw_input('Choose the Card Number: ')
    p_card = p2_hand.pop(int(card_choice)-1)

    return p_card, p2_hand


def computer_play(p1_hand, discard_pile):
    # Chooses a card from computer's hand
    # RETURNS:
    #       - Card chosen
    #       - New computer hand
    """
    >>> # Computer matches Ace when only card in hand
    >>> p1_hand = [12]
    >>> discard_pile = [25]
    >>> computer_play(p1_hand, discard_pile)
    (12, [])
    >>> # Computer matches King when there are four cards in hand
    >>> p1_hand = [7, 11, 17, 21]
    >>> discard_pile = [12, 24]
    >>> computer_play(p1_hand, discard_pile)
    (11, [7, 17, 21])
    >>> # Computer plays top card when it can't match
    >>> p1_hand = [7, 11, 17, 21]
    >>> discard_pile = [23]
    >>> computer_play(p1_hand, discard_pile)
    (21, [7, 11, 17])
    >>> # Computer doesn't play Jack if the discard pile is empty and it has 2 cards
    >>> p1_hand = [29, 35]
    >>> discard_pile = []
    >>> computer_play(p1_hand, discard_pile)
    (29, [35])
    """

    time.sleep(1)
    if len(discard_pile) == 0:
        # Don't play a Jack or Ace if the discard pile is empty
        for i in p1_hand:
            if Card_Deck[i]['value'] not in ['J', 'A']:
                p1_hand.remove(i)
                return i, p1_hand
        return p1_hand.pop(), p1_hand

    for i in p1_hand:
        if Card_Deck[i]['value'] == Card_Deck[discard_pile[-1]]['value']:
            p1_hand.remove(i)
            return i, p1_hand
    return p1_hand.pop(), p1_hand


def play(player, discard_pile, p1_hand, p2_hand, p1_pile, p2_pile, p1_pisti, p2_pisti, last_capture):
    # Calls computer play or player's function to allow card choice
    # Evaluates if capture occurred. Adjusts new discard pile, player piles,
    # player hands, pisti count and last capture code.
    # RETURNS:
    #            card played, discard pile, pisti count and last capture code

    if player == 1:
        p_card, p1_hand = computer_play(p1_hand, discard_pile)  # Computer turn: last card played (~random play)
    else:
        p_card, p2_hand = choose_card(p2_hand)

    try:
        top_card_value = Card_Deck[discard_pile[-1]]['value']
    except IndexError:  # If discard pile is empty, card is simply added to pile
        discard_pile.extend([p_card])
        return p_card, discard_pile, p1_pisti, p2_pisti, last_capture

    # If the discard pile is not empty, it is checked if a capture occurred.
    # The player pairs with the top card of the pile and takes pile
    if Card_Deck[p_card]['value'] == top_card_value:
        discard_pile.extend([p_card])
        # Cards get added to player1's pile
        if player == 1:
            p1_pile.extend(discard_pile)
            last_capture = 1
            # Check for Double Pisti
            if len(discard_pile) == 2 and Card_Deck[discard_pile[-1]]['value'] == "J":
                p1_pisti += 2
            # Check for Pisti
            elif len(discard_pile) == 2:
                p1_pisti += 1
        # Or to player2's pile
        else:
            p2_pile.extend(discard_pile)
            last_capture = 2
            # Check for Pisti
            if len(discard_pile) == 2 and Card_Deck[discard_pile[-1]]['value'] == "J":
                p2_pisti += 2
            # Check for Pisti
            elif len(discard_pile) == 2:
                p2_pisti += 1
        discard_pile = []

    # Player plays a jack and  discard pile is not empty -> pile is captured
    elif Card_Deck[p_card]['value'] == "J" and discard_pile:
        discard_pile.extend([p_card])
        # Cards get added to player1's pile
        if player == 1:
            p1_pile.extend(discard_pile)
            last_capture = 1
        # Or to player2's pile
        else:
            p2_pile.extend(discard_pile)
            last_capture = 2
        discard_pile = []

    # The player doesn't take the pile and the round continues
    else:
        discard_pile.extend([p_card])
    return p_card, discard_pile, p1_pisti, p2_pisti, last_capture


def deal_more(p1_hand, p2_hand, deck):
    # Draws four cards for each players' hand and removes them from the deck
    # Returns new player hands' and new reduced deck
    """
    >>> p1 = p2 = []
    >>> d = range(40)
    >>> random.shuffle(d)
    >>> p1, p2, d = deal_more(p1, p2, d)
    >>> len(p1) == len(p2) == 4
    True
    >>> len(d)
    32
    >>> set(p1) != set(p2)
    True
    """

    p1_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in p1_hand]

    # Draw four cards for player2's hand and remove them from the deck
    p2_hand = random.sample(deck, 4)
    deck = [x for x in deck if x not in p2_hand]

    return p1_hand, p2_hand, deck


def score(p1_pile, p2_pile, p1_pisti, p2_pisti):
    # Scores the hand at the end of the game
    # RETURNS: Players' scores

    """
    >>> p1_pile = [4, 23, 18, 21, 6, 2, 34, 31, 5, 10, 35, 32, 9, 27, 19, 16, 3, 22, 45, 46, 13, 43]
    >>> p2_pile = [17, 40, 15, 36, 38, 49, 11, 41, 39, 48, 42, 47, 50, 12, 7, 29, 44, 51, 0, 1, 8, 14, 20, 24, 25, 26, 28, 30, 33, 37]
    >>> p1_pisti = 2
    >>> p2_pisti = 1
    >>> score(p1_pile, p2_pile, p1_pisti, p2_pisti)
    (28, 18)
    >>> p1_pile = []
    >>> p2_pile = range(52)
    >>> p1_pisti = p2_pisti = 0
    >>> score(p1_pile, p2_pile, p1_pisti, p2_pisti)
    (0, 16)
    >>> p1_pile = random.sample(range(52), 26)
    >>> p2_pile = [x for x in range(52) if x not in p1_pile]
    >>> p1_pisti = p2_pisti = 0
    >>> sum(score(p1_pile, p2_pile, p1_pisti, p2_pisti))
    13
    """

    p1_scores = []
    p2_scores = []

    # Add one point for each Ace and Jack
    p1_scores.extend([1 for i in p1_pile if (Card_Deck[i]['value'] == "J" or Card_Deck[i]['value'] == "A")])
    p2_scores.extend([1 for i in p2_pile if (Card_Deck[i]['value'] == "J" or Card_Deck[i]['value'] == "A")])

    # Add two points for the 2 of Clubs (Card Code 13)
    if 13 in p1_pile:
        p1_scores.extend([2])
    else:
        p2_scores.extend([2])

    # Add three points for the 10 of Diamonds
    if 34 in p1_pile:
        p1_scores.extend([3])
    else:
        p2_scores.extend([3])

    # Add three points for the card majority
    if len(p1_pile) > len(p2_pile):
        p1_scores.extend([3])
    elif len(p2_pile) > len(p1_pile):
        p2_scores.extend([3])

    # Add points for the Pistis
    p1_scores.extend([10*p1_pisti])
    p2_scores.extend([10*p2_pisti])

    # Calculate the total scores
    p1_score = sum(p1_scores)
    p2_score = sum(p2_scores)

    return p1_score, p2_score


def game():
    # Sets up initial game and executes main looping through plays
    # RETURNS: Prints player's scores at the end of the game
    # RETURNS: (game variables to use for command line inspection if desired)

    deck, p1_hand, p2_hand, discard_pile, p1_pile, p2_pile = deal_initial()
    last_capture = 0  # Indicates which player took the last pile
    p1_pisti = p2_pisti = 0  # Initial pisti count is set to 0

    print("\nGood Luck!\n")
    for i in range(48):
        # Determine player
        player = 1 if (i % 2 == 0) else 2
        print("Turn: " + str(i+1) + (" (YOUR PLAY)" if player == 2 else "") + "\n==========")
        print("Discard Pile :" + str(len(discard_pile)) + " cards high")
        try:
            top_discard_card = Card_Deck[discard_pile[-1]]['value']+" of "+Card_Deck[discard_pile[-1]]['suit']
        except IndexError:
            top_discard_card = "empty"
        print("Top Card :"+top_discard_card+"\n")
        try:
            p_card, discard_pile, p1_pisti, p2_pisti, last_capture = play(player, discard_pile, p1_hand, p2_hand, p1_pile, p2_pile, p1_pisti, p2_pisti, last_capture)
        except IndexError:  # Player's hands have run out of cards
            p1_hand, p2_hand, deck = deal_more(p1_hand, p2_hand, deck)
            p_card, discard_pile, p1_pisti, p2_pisti, last_capture = play(player, discard_pile, p1_hand, p2_hand, p1_pile, p2_pile, p1_pisti, p2_pisti, last_capture)
        print("Player "+str(player)+" plays "+Card_Deck[p_card]['value']+" of "+Card_Deck[p_card]['suit'])
        print("P1 Hand: "+str(len(p1_hand))+" cards left")
        print("P2 Hand: "+str(p2_hand))
        # print("P1 Pistis: "+str(p1_pisti))
        # print("P2 Pistis: "+str(p2_pisti))
        print("P1 Pile: "+str(len(p1_pile))+" cards high")
        print("P2 Pile: "+str(len(p2_pile))+" cards high")
        print(" ")

    if last_capture == 1:
        p1_pile.extend(discard_pile)
    else:
        p2_pile.extend(discard_pile)
    discard_pile = []  # Empty discard pile for completion
    p1_score, p2_score = score(p1_pile, p2_pile, p1_pisti, p2_pisti)

    print("The game is over!")
    print("Player 1 scored: "+str(p1_score))
    print("Player 2 scored: "+str(p2_score))
    if p1_score > p2_score:
        print("Player 1 won the game.")
    elif p1_score < p2_score:
        print("Player 2 won the game.")
    else:
        print("You tied. Play again to settle this matter!")
    return deck, p1_hand, p2_hand, discard_pile, p1_pile, p2_pile, p1_pisti, p2_pisti


if __name__ == "__main__":
    import doctest
    doctest.testmod()
