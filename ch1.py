# Chapter 1: Clean Code
# Based on its name, you might assume that destroy_wall destroys a single wall, but if you look closely, you'll see that it handles multiple walls.


# 1 Welcome to OOP
# The test suite expects a different function name. Take a look at the main_test.py file to see what it's looking for, and rename the function accordingly.
# Bonus: rename the variables inside the function to be more descriptive.
def destroy_walls(walls):
    destroyed = []
    for wall in walls:
        if wall > 0:
            destroyed.append(wall)
    return destroyed

# 2 DRY code

# Your manager noticed that "Age of Dragons" has a lot of repetitive code. She's asked you to update the fight_soldiers function so that the DPS (damage-per-second) calculation is only written once.
# Notice how these two lines are practically identical:
# soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
# soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
# Create a new function called get_soldier_dps that takes a soldier and returns its DPS using the same logic as the lines above.
# Replace the two lines above with calls to get_soldier_dps.

def fight_soldiers(soldier_one, soldier_two):
    def get_soldier_dps(soldier):
        return soldier["damage"] * soldier["attaks_per_second"]
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
