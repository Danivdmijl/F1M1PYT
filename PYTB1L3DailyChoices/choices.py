print("Daily Choices")

print("Je gaat keuzes maken en gebasseerd daarop krijg je antoord!")


print("Je wekker gaat het is 6:30, SNOOZE jij of word je WAKKER ?")
choice = input()
if choice == 'SNOOZE':
    print("Je hebt je alarm uitgesteld, hier word je waarschijnlijk alleen maar moeier van..")
elif choice == 'WAKKER':
    print("Je word helemaal fris wakker en begint je dag!")
else:
    print(choice, " Dit is geen antwoord die je kon invoeren")

print("Oke oke,")

print("Je moet naar het station, neem je de BUS of pak je de FIETS ?")
choice = input()
if choice == 'BUS':
    print("Oke je nam de bus, je bent lekker optijd!")
elif choice == 'FIETS':
    print("Je gaat naar de scheur en er staan allemaal fietsen voor. Nu heb je hem eindelijk te pakken en fiets je naar station. Gelukig ben je nog wel op tijd!")
else:
    print(choice, " Dit is geen antwoord die je kon invoeren")

print("Gelukkig ben je optijd!")

print("Je staat op station te wachten op de trein maar, moet je LANGER of KORTER reizen dan 1 uur ?")
choice = input()
if choice == 'LANGER':
    print("Dat is minder..")
elif choice == 'KORTER':
    print("Dat is fijn, je hoefd gelukkig geen uren te reizen voor je thuis of op school/werk bent!")
else:
    print(choice, " Dat is geen antwoord die je kon invullen..")

print("Interesant,")

print(" Je komt aan op besteming LOOP jij of neem je de BUS naar de eindbesteming ?")
choice = input()
if choice == 'LOOP':
    print("Oke hopelijk is het niet al te ver.")
elif choice == 'BUS':
    print("Lekker zitten, hopelijk is het niet te druk!")
else:
    print(choice, " Dit was geen antwoord dat je kon invullen!")

print("Nicee")

print(" Je bent nu aangekomen maar ben je nu op SCHOOL of WERK ?")
choice = input()
if choice == 'SCHOOL':
    print("Veel succes!")
elif choice == 'WERK':
    print("Veel succes!")
else:
    print(choice, " DIt was geen antwoord dat je kon invullen!")

print("Dat was hem alweer, bedankt voor het meedoen!")