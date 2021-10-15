from array import *
import time

while True:

    factory = ["Auto"]
    distribution = ["Auto"]
    shop = ["Auto"]

    print("Fabriek:", factory )
    factory.pop(0)
    time.sleep(1)
    print("Fabriek:", factory)

    time.sleep(1)

    print("Verdeling:", distribution)
    distribution.pop(0)
    time.sleep(1)
    print("Verdeling:", distribution)

    time.sleep(1)

    print("Winkel:", shop)
    shop.pop(0)
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