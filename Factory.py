from array import *
import time
import os

while True:

    factory = ["Auto"]
    distribution = []
    shop = []

    print("Fabriek:", factory)
    print("Verdeling", distribution)
    print("Winkel:", shop)
    time.sleep(1)
    os.system('cls')
    popped_from_factory = factory.pop(0)
    distribution.append(popped_from_factory)
    os.system('cls')
    print("Fabriek:", factory)
    print("Verdeling", distribution)
    print("Winkel:", shop)

    time.sleep(1)
    os.system('cls')

    print("Fabriek:", factory)
    print("Verdeling", distribution)
    print("Winkel:", shop)
    popped_from_distribution = distribution.pop(0)
    shop.append(popped_from_distribution)
    time.sleep(1)
    os.system('cls')
    print("Fabriek:", factory)
    print("Verdeling", distribution)
    print("Winkel:", shop)

    time.sleep(1)
    os.system('cls')

    print("Fabriek:", factory)
    print("Verdeling", distribution)
    print("Winkel:", shop)
    popped_from_shop = shop.pop(0)
    
    time.sleep(1)
    os.system('cls')
    print("Fabriek:", factory)
    print("Verdeling", distribution)
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