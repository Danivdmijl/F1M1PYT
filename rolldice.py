import random
def roll_dice():
    random_getal = random.randrange(1, 50)
    return random_getal

rl = roll_dice()
print(rl)