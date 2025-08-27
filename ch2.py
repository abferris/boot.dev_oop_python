# Chapter 2: Classes

# 1 Classes

# Create a class called Wall. It should have:
# A property called armor initialized to (initially set to) 10
# A property called height initialized to 5
# Create a class called BatteringRam. It should have:
# A property called damage initialized to 2
# A property called length initialized to 4

class Wall:
    armor = 10
    height = 5


class BatteringRam:
    damage = 2
    length = 4

# 2 Methods
# Complete the fortify() method on the wall class. It should double the current armor property.

class FortifyingWall(Wall):
    def fortify(self):
        self.armor *=2 

# 3 Methods can Return

# Complete the .get_cost() method on the Wall class. It should return the cost of a wall, where the cost is its armor multiplied by its height.

class AppraisableFortifyingWall(FortifyingWall):
    def get_cost(self):
        return self.armor * self.height

# 4 Constructors
# we should be using constructors to define default values, as well as accept inputs. Its safer and allows for customization of objects
# use constructors to create a new Wall class that takes depth, height, and width, and has a calculated vlaue of volume

class BetterWall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
    @property
    def volume(self):
        return self.depth * self.height * self.width

# 5 Multiple Objects

# Take a look at the Brawler class and the fight function provided, then complete the main function by doing the following:

# Create 4 new brawlers with the following stats:
# Name: Aragorn. Speed: 4. Strength: 4.
# Name: Gimli. Speed: 2. Strength: 7.
# Name: Legolas. Speed: 7. Strength: 7.
# Name: Frodo. Speed: 3. Strength: 2.
# Call fight twice:
# The first fight should be Aragorn vs Gimli.
# The second will be Legolas vs Frodo.

def rumble():
    human = Brawler("Aragorn",4,4)
    dwarf = Brawler("Gimli",2,7)
    elf = Brawler("Legolas", 7,7)
    hobbit = Brawler("Frodo", 3,2)
    fight(human,dwarf)
    fight(elf,hobbit)


# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(f1, f2):
    print(f"{f1.name}: {f1.power} power")
    print(f"{f2.name}: {f2.power} power")
    if f1.power > f2.power:
        print(f"{f1.name} wins!")
    elif f1.power < f2.power:
        print(f"{f2.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")

# 6 Archer Practice

# Complete the Archer class.

# I mixed things in this one up to be more to my liking

# Complete the constructor. It should take the following parameters in order and set them as instance properties:
# name
# health
# num_arrows
# Complete the take_hit method. It operates on the current archer instance.
# Remove one health from the current archer.
# If the archer has no health, raise the exception: {NAME} is dead where {NAME} is the archer's name.
# Finish the shoot method. It takes an Archer instance as its target input.
# If the shooter has no arrows left, raise an exception {NAME} can't shoot where {NAME} is the shooter's name.
# Otherwise, remove an arrow from the shooter.
# Print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted arch

class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.max_health = health
        self.health = health
        self.num_arrows = num_arrows
    
    @property 
    def alive(self):
        if self.health == 0 :
            return False
        else :
            return True


    def take_hit(self):
        if self.health == 0 or self.alive == False: 
            raise Exception(f"{self.name} is already dead")
        self.health -= 1
        if self.health == 0:
            print("Damage Taken: {self.name} is dead")
        else:    
            print( f"Damage Taken: {self.health}/{self.max_health} health remaining for {self.name}")

    def shoot(self, target):
        if self.alive == False:
            raise Exception(f'{self.name} cannot shoot! They are dead!!')
        if self.num_arrows == 0:
            raise Exception(f'{self.name} cannot shoot! No ammo!')
        else :
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
            target.take_hit()

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows, self.alive

    def print_status(self):
        print(f"{self.name} has {self.health}/{self.max_health} health and {self.num_arrows} arrows")


# 7 Class Variables vs. Instance Variables

# In the main() function (that our team isn't responsible for) the line: Dragon.element = "fire"
# should not affect our existing Dragon instances! The Dragon class should be safe to use in other parts of the codebase, even if silly developers are out there changing class-level variables.

# Fix the Dragon class.

# Remove the element class variable. Use an instance variable for element, and allow it to be set in the constructor.

class Dragon:

    def __init__(self, element="ice"):
        self.element = element
        return

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


# don't touch below this line


def run_dragon():
    first_dragon = Dragon("fire")
    print(f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage")
    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage")

# 8 Classes Practice
# Create the Book Class:
# Create the __init__(self, title, author) method
# Set .title and .author to the values of the parameters.
# Create the Library Class:
# Create the __init__(self, name) method
# Initialize a .name member variable to the value of the name parameter.
# Create a .books member initialized to an empty list.
# Add the add_book(self, book) method:
# Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
# Add the remove_book(self, book) method:
# Create a new, empty list to hold the books you want to keep.
# Loop through every book in the library’s books list.
# If the book’s title or author do not match the one you want to remove, add it to the new list.
# After checking all the books, replace the library’s books list with the new list.
# Add the search_books(self, search_string) method:
# For every book in the library check if the search_string is contained in the title or author field (case-insensitive).
# Return a list of all books that match the search string, ordered in the same order as they were added to the library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
   

    def add_book(self, book:Book):
        self.books.append(book)

    def remove_book(self, book):
        for index,lit in enumerate(self.books) :
            if lit.title == book.title and lit.author == book.author :
                self.books.pop(index)
        return self.books
    def search_books(self, search_string):
        output = []
        for book in self.books:
            if search_string.casefold() in book.title.casefold() or search_string.casefold() in book.author.casefold():
                output.append(book)
        return output