# Chapter 4: Abstraction

# 1 Abstraction
# Complete the following methods in the Human class:

# move_right(): Adds the human's speed to its x position.
# move_left(): Subtracts the human's speed from its x position.
# move_up(): Adds the human's speed to its y position.
# move_down(): Subtracts the human's speed from its y position.
# get_position(): Returns the x position and y position as a tuple.

class Human:
    def __init__(self, pos_x, pos_y, speed, name="Bob"):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.name = name

    @property
    def position(self):
        return self.__pos_x, self.__pos_y

    def move_right(self):
        self.__pos_x += self.__speed
        return self.position

    def move_left(self):
        self.__pos_x -= self.__speed
        return self.position

    def move_up(self):
        self.__pos_y += self.__speed
        return self.position

    def move_down(self):
        self.__pos_y -= self.__speed
        return self.position

# 2 Sprint

class FastHuman(Human):
    def __init__(self, pos_x, pos_y, speed, stamina):
        super().__init__(pos_x,pos_y,speed)
        self.__stamina = stamina

    def sprint_right(self):
        self.__use_sprint_stamina
        self.move_right()
        self.move_right()
        return self.position

    def sprint_left(self):
        self.__use_sprint_stamina
        self.move_left()
        self.move_left()
        return self.position

    def sprint_up(self):
        self.__use_sprint_stamina
        self.move_up()
        self.move_up()
        return self.position

    def sprint_down(self):
        self.__use_sprint_stamina
        self.move_down()
        self.move_down()
        return self.position

    def __raise_if_cannot_sprint(self):
        if self.__stamina == 0:
            raise ValueError("Not Enough Stamina to Sprint")
        return "Can Sprint"

    def __use_sprint_stamina(self):
        self.__raise_if_cannot_sprint()
        self.__stamina -= 1
        return "Sprinting"

# 3 Abstraction Practice

# Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided for you as class variables. You won't need to modify them, but you will need to use them.

# Complete the constructor:
# Initialize a private empty list called cards.
# Fill that empty list by calling the create_deck method within the constructor.
# Complete the create_deck(self) method:
# Create a (Rank, Suit) tuple for all 52 cards in the deck and append them to the cards list.
# Order matters! The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

# Complete the shuffle_deck(self) method:
# Use the random.shuffle() function (available from the random package) to shuffle the cards in the deck.
# Complete the deal_card(self) method:
# .pop() the first card off the top of the deck (top of the deck is the end of the list) and return it. If there are no cards left in the deck the method should instead return None

import random


class DeckOfCards:

    def __init__(self):
        self.__SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.__RANKS = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.__SUITS:
            for rank in self.__RANKS:
                card = suit, rank
                self.__cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        else:
            card = self.__cards.pop()
            return card
    @property
    def count(self):
        return len(self.__cards)
    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"

