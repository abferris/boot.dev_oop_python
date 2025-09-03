# Chapter 5: Inheritance

import copy
# I've already been doing this, so we will try to breeze through this

#1 Inheritance
# Complete the Archer class. It should inherit the Human class.

# Its constructor should:
# Call the parent constructor
# Set the private __num_arrows property based on the constructor parameter
# Its get_num_arrows() method should return the number of arrows the archer has.

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        Human.__init__(self,name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.get_num_arrows() < num:
            raise Exception("not enough arrows")
        else :
            self.__num_arrows -= num
        return self.get_num_arrows()
    

# 2 Inheritance Hierarchy

# Complete the use_arrows method on the Archer class. It should remove num arrows, but if there aren't enough arrows to remove, it should raise a not enough arrows exception instead.
# DOING THIS ABOVE

# Complete the Crossbowman class.
# Its constructor should call its parent's constructor.
# Its triple_shot method should:
# Use 3 arrows
# Return the string TARGET was shot by 3 crossbow bolts where TARGET is

class Crossbowman(Archer):
    # def __init__(self, name, num_arrows):
    #     pass

    def triple_shot(self, target:Human):
        self.use_arrows(3)
        return f"{target.get_name()} was shot by 3 crossbow bolts"

# 3 Multiple Children

# Assignment
# Ensure the following requirements from the game designers are completed:

# Archer should inherit from Hero.
# HERO WILL INHERIT HUMAN

# Archer should set up the hero's name and health.
# Add a private "number of arrows" variable that can be set by the constructor.
# Complete the shoot method. It takes a target hero as input.
# If there are no arrows left, raise a not enough arrows exception.
# Otherwise, remove an arrow and deal 10 damage to the target hero.

class Hero(Human):
    def __init__(self, name, health):
        Human.__init__(self,name)
        self.__health = health

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class HeroArcher(Hero, Archer):
    def __init__(self, name, health, num_arrows):
        Hero.__init__(self, name, health)
        Archer.__init__(self, name, num_arrows)

    def shoot(self, target: Hero):
        if self.get_num_arrows() <= 0:
            raise Exception("not enough arrows")
        self.use_arrows(1)
        target.take_damage(10)
        return f"{self.get_name()} has shot {target.get_name()}. {target.get_name()} takes 10 damage and has {target.get_health()} health left."
    
# 4 Complete the Wizard class.

# Wizard should inherit from Hero.
# Wizard should set up the hero's name and health.
# Set a private mana variable that can be passed in as a third parameter to the constructor.
# Create a cast method that takes a target hero as input.
# If there is less than 25 mana left, raise a not enough mana exception.
# Otherwise, remove 25 mana from the wizard and deal 25 damage to the target hero.

class Wizard(Hero):
    def __init__(self, name, health, mana):
        Hero.__init__(self, name, health)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def use_mana(self, num):
        if self.get_mana() < num:
            raise Exception("not enough mana")
        else :
            self.__mana -= num
        return self.get_mana()

    def cast(self, target: Hero):
        self.use_mana(25)
        target.take_damage(25)
        return f"{self.get_name()} has cast a spell at {target.get_name()}. {target.get_name()} takes 25 damage and has {target.get_health()} health left."               


# 5 Dragons

# Complete the following methods:

# Complete the unit's in_area method. It accepts an "area" represented by four points: x_1, y_1, x_2, and y_2. The coordinates x_1 and y_1 represent the bottom-left corner, while x_2 and y_2 represent the top-right corner.
# Determine if the unit is within the given area by using the unit's position coordinates pos_x and pos_y.
# Return True if the unit's position falls inside or on the edge of the rectangle. Otherwise, return False.
# Complete the dragon's breathe_fire method. It causes the dragon to breathe a swath of fire at the target area.
# The target area is centered at (x, y). The area stretches for __fire_range in both directions inclusively.
# Iterate over each unit in the units list, and check if the unit is in the area. If it is, add it to a new list that keeps track of the units hit by the blast.
# Return the list of units hit by the blast.

class Unit:
    def __init__(self, name, pos_x=0, pos_y=0):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def get_name():
        return self.name

    def in_area(self, x_1, y_1, x_2, y_2):

        if self.pos_x >= x_1 and self.pos_x <= x_2  and self.pos_y >= y_1 and self.pos_y <= y_2 :
            return True
        return False


class Dragon(Unit):
    def __init__(self, name,fire_range, pos_x=0, pos_y=0 ):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_hit = []
        x_max = x + self.__fire_range
        x_min = x - self.__fire_range
        y_max = y + self.__fire_range
        y_min = y - self.__fire_range
        print("====================================")
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("------------------------------------")
        for unit in units:
            if isinstance(unit,Unit) == False:
                raise TypeError("Target is not a unit!")
            if unit.in_area(x_min,y_min,x_max,y_max):
                units_hit.append(unit)
                print(f"{unit.name} is hit by the fire from {self.name}")
        return units_hit

# 6 Dragon Fight

# Complete the bottom half of the main() function using two for-loops:

# Iterate over all the dragons and describe() each one in order.
# Iterate over all the dragons again and have each dragon breathe_fire at coordinate x=3, y=3. Pass in all the other dragons (not the one currently breathing fire) as the units parameter, so we can see if they get hit.
# Pass in the dragons in the same order as the original list, excluding the current dragon. For example, when Blue Dragon breathes fire, it should check to breathe fire on the other dragons in this order:

# Green Dragon
# Red Dragon
# Black Dragon
def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")

def start_dragon_fight():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]
    for dragon in dragons:
        describe(dragon)

    for index,dragon in enumerate(dragons):
        targets = dragons.copy()
        targets.pop(index)
        dragon.breathe_fire(3,3,targets)


# 7 Inheritance Practice

# Finish implementing the empty methods of the Rectangle and Square classes. All squares are rectangles, but not all rectangles are squares.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
        
    @property
    def perimeter(self):
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        self.width = length

# 8 Inheritance Practice 2 
# Complete the Siege, BatteringRam, and Catapult classes:

# Complete the Siege class:
# Complete the constructor. It accepts two parameters (in order) and sets them as public instance variables with the same name: max_speed and efficiency
# Complete the get_trip_cost() method. It calculates the cost of a trip and returns it. The formula for calculating the cost is: (distance / efficiency) * food_price. It costs food to move siege weapons, those things are heavy!
# Leave the get_cargo_volume() method as empty. Use the pass keyword. Child classes will override this method.
# Complete the BatteringRam class:
# Complete the constructor. It calls the parent constructor, then sets the extra battering-ram-only instance variables as member variables.
# The get_trip_cost() method uses the parent get_trip_cost() method to calculate the cost of food for a trip, plus the extra cost of carrying a load. The formula for calculating the cost: get_trip_cost() + (load_weight * 0.01)
# The get_cargo_volume() method calculates and returns the cargo capacity in cubic meters. To get the volume of the battering-ram's 'cargo' (bed_area), multiply its area by its depth, which is always 2 meters.
# Complete the Catapult class:
# The constructor calls the parent constructor, then sets the extra catapult-only instance variable as a member variable.
# Do not override the get_trip_cost() method. It's inherited from the parent class.
# The get_cargo_volume() method just returns the cargo capacity of the catapult. This is already set by the constructor.

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance/ self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(self, max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        original_cost = super().get_trip_cost()
        additional_cost = self.load_weight*.01
        return original_cost + additional_cost
    def get_cargo_volume(self):
        return bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().init(self, max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
