antwoord = 2
vraag = ("Wat is 1+1")
while True:
    print(vraag)
    hallo = input()
    if hallo == str(antwoord):
        print("Goed gedaan dat is goed")
        break
    else: print("Dat is fout, probeer het opnieuw")