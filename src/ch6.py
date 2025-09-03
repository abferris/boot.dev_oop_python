# Chapter 6: Polymorphism

# 1 Polymorphism

# Let's build some hit-box logic for our game, starting with a simple Rectangle.

# Complete the __init__() method. Configure the class to have properties matching the variables passed into the constructor in this order: x1, y1, x2, y2


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2



# 2 Get Edges

#Complete the following methods:

# get_left_x(): Returns the leftmost (smallest) x value
# get_right_x(): Returns the rightmost (largest) x value
# get_top_y(): Returns the topmost (largest) y value
# get_bottom_y(): Returns the bottom-most (smallest) y value

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

# 3 Overlap

# Complete the overlaps() method. It should check if the current rectangle (self) overlaps a given rectangle (rect).

# Return True if self overlaps any part of rect, including just touching sides. Return False otherwise.

    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )



# 4 Dragon Area 
# Complete the Dragon's constructor:
# Call constructor of the Unit class with the provided parameters
# Set the dragon-specific parameters as instance variables
# Create a new private __hit_box member. It's a Rectangle object representing the dragon's hit box. See the tips below if you need help.
# Override the in_area method in the Dragon class:
# Create a new rectangle object with the given corner positions.
# Use the rectangle's overlaps method to check if the Dragon's self.__hit_box is inside it, and return the

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(self,name,pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range

    @property
    def hit_box(self) :
        x1 = pos_x - (width/2)
        x2 = pos_x + (width/2)
        y1 = pos_y - (height/2)
        y2 = pos_y - (height/2)
        return Rectangle(x1,y1,x2,y2)

    def in_area(self, x1, y1, x2, y2):
        rect = Rectangle(x1,y1,x2,y2)
        return rect.overlaps(self.hit_box)


# 5 Operator Overloading

# Create an __add__(self, other) method on the Sword class.

# If two "bronze" swords are crafted together, return a new Sword of type "iron".
# If two "iron" swords are crafted together, return a new Sword of type "steel".
# If a player tries to craft anything other than 2 bronze swords or 2 iron swords, just raise an Exception with the message "cannot craft".

class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type != other.sword_type:
            raise Exception("cannot craft")
        elif self.sword_type == "bronze":
            print("crafting iron sword")
            return Sword("iron")
        elif self.sword_type == "iron":
            print("crafting steel sword")
            return Sword("steel")

#6 Overriding Built-In Methods

# When print() is called on an instance of a Drake, the string I am NAME, the COLOR dragon should be printed.
# Where NAME is the name of the dragon, and COLOR is its color.

class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name} the {self.color} dragon"

# 7 Polymorphism Practice

Complete the Card class:

# Define a constructor that takes rank and suit as parameters and sets rank, suit, rank_index, and suit_index instance variables.
# You will need the indexes of the ranks, and suits to help you compare them against each other. Keep in mind that a rank and a suit are just strings within a list.
# Overload the following comparison operators:
# ==: __eq__
# >: __gt__
# <: __lt__

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index =  SUITS.index(suit)
        self.card_value = rank_index + (suit_index/4)

    def __eq__(self, other):
        return self.card_value == other.card_value

    def __lt__(self, other):
        return self.card_value < other.card_value

    def __gt__(self, other):
        return self.card_value > other.card_value

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# 8 Polymorphism
# Finish the Round Class and its two children Classes
# HighCardRound: The highest card wins
# LowCardRound: The lowest card wins
# Complete the HighCardRound class that inherits from Round:
# Create a constructor that takes two cards (card1 and card2) and stores them as instance variables.
# Implement the resolve_round() method that returns:
# 1 if card1 is higher than card2
# 2 if card2 is higher than card1
# 0 if the cards are equal
# Complete the LowCardRound class that inherits from Round:
# Create a constructor that takes two cards (card1 and card2) and stores them as instance variables.
# Implement a resolve_round() method that returns:
# Return player number of winner
# if tie return both

# Changing to 

class Round:
    def __init__(self, *cards)
        if len(cards) == 0:
            raise Exception("No cards in round")
        self.cards = cards
        self.winner = None
        self.winner_player = []
    def resolve_round(self):

        raise NotImplementedError("Subclasses must implement resolve_round()")


# Don't touch above this line


class HighCardRound(Round):
    def resolve_round(self):
      
        for idx, card in enumerate(cards):
            if len(self.winner_index) == 0 or self.winner == card:
                self.winner = card
                self.winner_player.append(idx+1)
            elif self.winner[0] < card:
                self.winner = card
                self.winner_player = [idx+1]
        if len(self.winner_player) == 1 :
            winner_player_str = self.winner_player[0]
            print(f("Player {winner_player_str} wins with the {self.winner}"))
        
        else len(self.winner_idx) >= 0 :
            winner_player_str = ' '.join(map(str, self.winner_player))
            print(f("Players {winner_player_str} tie with the {self.winner}"))
        return self.winner_player

    
    


class LowCardRound(Round):
      
        for idx, card in enumerate(cards):
            if len(self.winner_index) == 0 or self.winner == card:
                self.winner = card
                self.winner_player.append(idx+1)
            elif self.winner[0] > card:
                self.winner = card
                self.winner_player = [idx+1]
        if len(self.winner_player) == 1 :
            winner_player_str = self.winner_player[0]
            print(f("Player {winner_player_str} wins with the {self.winner}"))
        
        else len(self.winner_idx) >= 0 :
            winner_player_str = ' '.join(map(str, self.winner_player))
            print(f("Players {winner_player_str} tie with the {self.winner}"))
        return self.winner_player

        
