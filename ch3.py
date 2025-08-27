# Chapter 3: Encapsulation

# 1 Encapsulation
# Complete the Wizard class's constructor.

# Set 2 private properties (be sure to include the private __ prefix):
# stamina
# intelligence
# Set 3 public properties:
# name: Use the value passed into the constructor
# health: 100x the value of "stamina"
# mana: 10x the value of "intelligence"
# as a note, max values health and mana should exist and be calculated, so if stamina and intelligence are modified, the other values depending on those are updated.

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = intelligence * 10
        self.health = stamina * 100
        
    @property
    def max_health(self):
        return self.__stamina * 100
    @property
    def max_mana(self):
        return self.__intelligence * 10

# 2 Wizard Duel

# Complete the following methods on the Wizard class:

# get_fireballed() should:
# Reduce the fireball_damage by the wizard's __stamina
# Reduce the wizard's health by the resulting fireball_damage
# drink_mana_potion() should:
# Increase the potion_mana by the wizard's __intelligence
# Increase the wizard's mana by the resulting potion_mana
# Both methods operate directly on the instance of the class (self). They take one input and return no values explicitly.
# weird there is no mana cap

class FireballCatchingWizard(Wizard):
    # don't touch above this line

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage
        if self.health >= 0:
            return f"{self.name} got fireballed! {self.health} out of {self.max_health} remains."
        else:
            return f"{self.name} got fireballed! {self.health} has died."
    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana
        return f"{self.name} drank a potion. They gained {potion_mana} mana and has {self.mana} currently."
# 3 Wizard Duel: act 2
# Complete the cast_fireball method:
# If there isn't enough mana to cast a fireball (based on the fireball_cost argument), raise an Exception with the message ____ cannot cast fireball, where ____ is the wizard's name.
# If the wizard has enough mana, reduce their mana by the fireball_cost and call get_fireballed on the target wizard with the given fireball_damage.
# Complete the is_alive method. It should return True if the wizard's health is greater than 0 and False otherwise.
# i think is alive should be a property instead of a function
class FireballCastingWizard(FireballCatchingWizard):
    @property
    def is_alive(self):
        return self.health > 0
    
     def cast_fireball(self, target:FireballCatchingWizard, fireball_cost:int, fireball_damage:int):
        if fireball_cost > self.mana :
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost
        result = target.get_fireballed(fireball_damage)
        return f"{self.name} fireballed {target.name}. {result} {self.name} has {self.mana} left."

# 4 Encapsulation Practice
# Complete the constructor
# Set __account_number to account_number
# Set __balance to initial_balance
# Complete the public getters
# Complete the get_account_number method to get the value of the private variable __account_number and return it.
# Complete the get_balance method to get the value of the private variable __balance and return it.
# Complete the deposit method
# It should accept an amount as input and add it to the account balance.
# If the deposit amount isn't positive, it should raise a ValueError exception with the message cannot deposit zero or negative funds. Otherwise, it should add the amount to the balance.
# Complete the withdraw method
# It should accept an amount and check if there is enough money in the account for the withdrawal.
# If the withdrawal amount isn't positive, it should raise a ValueError exception with the message cannot withdraw zero or negative funds.
# Then, if there are not enough funds it should raise a ValueError exception with the message insufficient funds.
# Otherwise, it should deduct the amount from the balance.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount
        return f"{amount} deposited into account. {self.__balance} funds available"

    def withdraw(self, amount):
         if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        elif self.__balance < amount:
            raise ValueError("insufficient funds")
        self.__balance -= amount
        return f"{amount} withdrawn from account. {self.__balance} funds availableS"