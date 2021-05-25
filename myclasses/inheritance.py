import random

class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    """ A deck of Cards. """

    def __init__(self):
        self.cards = []
        for suit in [0,1,2,3]:
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        final_str = []
        for card in self.cards:
            final_str.append(str(card))

        return "\n".join(final_str)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

class Hand(Deck):
    """Represents a player's hand."""

    # Overriding a certain behavior
    def __init__(self, deck, num_of_cards_in_the_game):
        self.cards = []
        for i in range(num_of_cards_in_the_game):
            self.add_card(deck.pop_card())

    # All other methods in Deck are inherited!

    # New behavior being added!
    def __lt__(self, other):
        self.cards.sort()
        other.cards.sort()
        return self.cards[-1] < other.cards[-1]

# Create your deck & shuffle it!
mydeck = Deck()
mydeck.shuffle()

# Deal cards to Player/s
player1 = Hand(mydeck, 4)
player2 = Hand(mydeck, 4)

print(player1 > player2)

# Print Player's Hand
player1.pop_card()
print(player1)