"""
Action Deck Module
Dane Burchette
November 22, 2024
"""

from random import shuffle as _shuffle


class Card:

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit
        self.face = False
        self.joker = False

        self.set_rank_string()
        self.set_suit_string()

    def __str__(self):
        if self.joker:
            return f"{self.rank_str} {self.suit_str}"
        elif self.face:
            return f"{self.rank_str} of {self.suit_str}"
        else:
            return f"{self.rank} of {self.suit_str}"

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

    def __gt__(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        else:
            return self.rank > other.rank

    def set_suit_string(self) -> None:
        match self.suit:
            case 1:
                self.suit_str = "󰣎 Clubs"
            case 2:
                self.suit_str = "󱀝 Diamonds"
            case 3:
                self.suit_str = " Hearts"
            case 4:
                self.suit_str = "󰣑 Spades"
            case _:
                self.suit_str = "Joker"
                self.joker = True

    def set_rank_string(self) -> None:
        if self.rank < 2 or self.rank > 10:
            self.face = True
            match self.rank:
                case 1:
                    self.rank_str = "Ace"
                    self.rank = 14
                case 11:
                    self.rank_str = "Jack"
                case 12:
                    self.rank_str = "Queen"
                case 13:
                    self.rank_str = "King"
                case _:
                    if self.rank == 0:
                        self.rank_str = "Red"
                    else:
                        self.rank_str = "Black"
                    self.rank = 15


class Deck:

    def __init__(self):
        self.active_cards = []
        self.discard = []
        self.make_deck()

    def make_deck(self) -> None:
        self.deck = [Card(x, y) for x in range(1, 14) for y in range(1, 5)]
        self.deck.append(Card(0, 14))
        self.deck.append(Card(15, 15))

    def shuffle(self) -> None:
        self.deck += self.discard
        self.discard.clear()
        _shuffle(self.deck)

    def discard(self, cards: list) -> None:
        self.discard += cards
        self.active_cards.clear()

    def draw(self) -> Card:
        card = self.deck.pop()
        return card

    def draw_x(self, count: int) -> list:
        cards = [self.draw() for i in range(1, (count+1))]
        return cards


if __name__ == "__main__":
    test = Deck()
    test.shuffle()
    hand = test.draw_x(5)
    for card in hand:
        print(card)
    hand.sort(reverse=True)
    print("sort")
    for card in hand:
        print(card)
