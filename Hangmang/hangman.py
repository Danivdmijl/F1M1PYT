import random
from words import word_list

secretword = word_list
lettersGuessed = ""

failurecount = 6

while failurecount > 0:

    guess = input("Gok een letter: ")

    if guess in secretword:
        print("Goedzo er is nog een letter in het woord.")
    else:
        failurecount -= 1
        print('Fout, die letter zit er niet in het woord.')
        print(failurecount, "beurten over")

    lettersGuessed = lettersGuessed + guess 
    wronglettercount = 0
    for letter in secretword:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercount += 1

    if wronglettercount == 0:
        print(f" Gefeliciteerd je hebt het woord geraden! Het woord was: {secretword}")
        break

else:
    print("Helaas je ben af!")