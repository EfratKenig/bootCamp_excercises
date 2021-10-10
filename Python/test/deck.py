import random


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 11):
            for j in self.Card.colors:
                self.cards.append(self.Card(j, i))

    # shuffle - the cards should be randomly rearranged.
    def shuffle(self):
        random.shuffle(self.cards)

    # deal - pop a card to the player.

    def deal(self):
        return self.cards.pop()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.cards):
            return self.deal()
        else:
            raise StopIteration

    class Card:
        colors = ['red', 'blue', 'green', 'yellow']

        def __init__(self, type, number):
            self.color = type
            self.number = number

        def __repr__(self):
            return '(' + str(self.number) + ', ' + str(self.color) + ')'
