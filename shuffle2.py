import random

original = input()

def randomizer(woord):
    randomised = ''.join(random.sample(woord, len(woord)))
    return randomised

for i in range(3):
    print(randomizer(original))
