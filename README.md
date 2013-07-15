Pisti Instructions and Comments
===================

Pisti (pronounced 'Pishti') is a Turkish card game using a standard 52 card pack.
Here it is played by two players, the computer and one human player.
[Wikipedia](http://en.wikipedia.org/wiki/Bastra)

Cards are dealt to a discard pile, here called discard pile. The goal of the game
is to get as many points possible by capturing the cards in the discard pile.
The discard pile can be captured by playing a jack or by matching the value of the previous card.
(e.g. By putting a 9 on top of a 9)

In the end, each player accumulates a stack of cards this way. Points are awarded to certain cards
and the winner is who accumulated more points overall.

A detailed description of the game follows. 

Cut 
--------------------

First, four cards each are dealt to Player 1 and Player 2. Four more cards are put in the discard pile,
the last one facing upwards. The remaining 40 cards are put in a stock of undealt cards. If the card facing
upwards is a jack it is returned to the bottom of the discard pile and the next card is placed face upwards.
(In the extremely unlikely case of all cards being jacks, cards are dealt again.)

Play
--------------------
Player 1 plays the first card. If the card matches the top card of the discard pile or is a jack,
he captures the pile. Otherwise, it is added to the discard pile.

Then Player 2 plays a card. If the card matches the top card of the discard pile or is a jack, she takes the pile.
Otherwise, it is added to the discard pile. If a player takes the pile, the other player will play the next card
and start a new discard pile.

Once both players have run out of cards in their hand, four more cards are dealt and the game continues. 

When all the cards have run out, the remaining discard pile is given to the player who made the last capture. 

Pisti
--------------------
A pisti occurs when the discard pile consists of only one card and the value of that card is matched by the player.
For example, the discard pile only consists of a 10 and the other player matches that ten. It is not possible
to score a pisti at the very beginning as the face-down cards also count.

Double pistis are awarded when a jack is played on a jack.

The very last card of the game, just before the scoring cannot score a pisti. 

Scoring
--------------------
Points are awarded for three different things: getting the majority of the cards, capturing specific cards
and for scoring pistis.

The scoring rules are as follows:
- each jack is worth 1 point
- each ace is worth 1 point
- the 2 of clubs is worth 2 points
- the 10 of diamonds is worth 3 points
- the card majority (i.e. 27 or more cards) is worth 3 points
- each pisti is worth 10 points or in the case of a jack on jack pisti 20 points

Winning
--------------------
The game is won by the player who scores more points.

(Normally, a match consists of several games and game points are added up until the first player reaches
151 points overall. In the current version, the match ends after one game.)

Modifications
--------------------
Some minor modifications from the original game have been made for this version of Pisti.

Most importantly, the computer plays a completely random strategy. It simply chooses the top card in its hand
which will be a random card. This, of course, makes beating the computer very easy.

Another alteration is that number of cards in the different piles are displayed at each turn. In a normal game
players do not have that information although they may count the cards or estimate the number of cards based on
the height of the card piles.

Development Plan
===================
There are two main aspects of the game that need to be developed further for the game to become interesting.

1. Computer Intelligence
--------------------
Currently the computer plays the computer plays a random strategy. This makes the game very boring as it is
almost impossible not to win. Therefore introducing some strategy into the computer's choices is a high
priority.

Most obviously, the computer should always play the matching card when it is able to do so. This is very quick
and easy to implement.

2. Web Application
--------------------
The command line interface used currently is obviously very unsuited to playing a card game. It is difficulty
to communicate the relevant information and is visually very unpleasant. A next step would be to make a web
application out of the game. This, however, is a fairly substantial project and the code of would most likely
have to be rewritten in javascript as well.


Change Log
===================
(Incomplete as only started recently)

* Change readme formatting to markdown
* Shorten comments for (sort of) pep8 compliance
* Rename & shorten variable names
* Rename functions names to be more descriptive
* Disallow card choice outside of player's card index
* Draw initial player cards without replacement
* Make sure that last card of initial discard pile is not a Jack
* Write scoring function
* Allow player 2 to choose cards
