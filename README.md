Pisti Instructions and Comments
===================

Pisti (pronounced 'Pishti') is a Turkish card game using a standard 52 card pack.
Here it is played by two players, the computer and one human player.
[Wikipedia](http://en.wikipedia.org/wiki/Bastra)

Cards are dealt to a central pile, here called discard pile. The goal of the game
is to get as many points possible by capturing the cards in the discard pile.
The discard pile can be captured by playing a jack or by matching the value of the previous card.
(e.g. By putting a 9 on top of a 9)

In the end, each player accumulates a stack of cards this way. Points are awarded to certain cards
and the winner is who accumulates more points overall.

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
he captures the pile. Otherwise, it is added to the discard pile - now five cards high.

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

1. The computer always begins the game. Usually, the players do turns in dealing the cards and
starting the game.
2. The number of cards in the different piles are displayed at each turn. In a normal game
players do not have that information although they may count the cards or estimate the number of cards based on
the height of the card piles.

How to Play
===================
1. Git clone the repository. No particular packages are required.
2. Open the python console and run `from game import *`
3. Type `game()`, hit enter and start playing!

Development Plan
===================
The primary area that has to be addressed at this point are usability and computer strategy.

1. Computer Intelligence
--------------------
Currently, a basic version of computer intelligence has been implemented. The computer captures the pile whenever
it can match a card. Jacks are still played randomly.

A next step would be to add more intelligence. For example, the computer could strategically play cards that minimize
the chance of an opponents capture if it can't capture the pile itself. It could also play the Jack strategically,
although this is a fairly complex problem.

2. Web Application
--------------------
The command line interface used currently is obviously very unsuited to playing a card game. It is difficulty
to communicate the relevant information and is visually very unpleasant. A next step would be to make a web
application out of the game. This, however, is a fairly substantial project and the code of would most likely
have to be rewritten in javascript as well.

3. Minor Bugfix
--------------------
The game right now would crash if the initial draw of the discard pile would consist exclusively of Jacks. This
is not a priority, however, as the chance of this happening is only 1 in 270'725.

Change Log
===================
(Incomplete as only started recently)

* Adding Computer Intelligence
* Change readme formatting to markdown
* Shorten comments for (sort of) pep8 compliance
* Rename & shorten variable names
* Rename functions names to be more descriptive
* Disallow card choice outside of player's card index
* Draw initial player cards without replacement
* Make sure that last card of initial discard pile is not a Jack
* Write scoring function
* Allow player 2 to choose cards
