from array import *
import time

while True:

    factory = ["Auto"]
    distribution = []
    shop = []

    print("Fabriek:", factory)
    popped_from_factory = factory.pop(0)
    distribution.append(popped_from_factory)
    time.sleep(1)
    print("Fabriek:", factory)

    time.sleep(1)

    print("Verdeling:", distribution)
    popped_from_distribution = distribution.pop(0)
    shop.append(popped_from_distribution)
    time.sleep(1)
    print("Verdeling:", distribution)

    time.sleep(1)

    print("Winkel:", shop)
    popped_from_shop = shop.pop(0)
    
    time.sleep(1)
    print("Winkel:", shop)
    time.sleep(1)

    start = input('Wil je het script nog eens afspelen? ja/nee ')
    if start == 'ja'.strip().lower():
        print("Oke, komt ie.")
        
    elif start == 'nee'.strip().lower():
        print("Adios")
        break
    else: 
        print("Dat kan niet alleen ja of nee..")
        break