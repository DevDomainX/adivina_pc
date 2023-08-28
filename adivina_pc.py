#!/usr/bin/env python3
from time import sleep
from random import randint


def pc():
    inte = 0
    while inte < 5:
        try:
            inte += 1
            ing = int(input("Ingrese un numero: "))
            sleep(2)
            num = randint(1, 50)
            print(num)

            if num == ing:
                print("found")
            else:
                print("no found")
        except ValueError:
            inte -= 1
            print("Ingrese solo numeros enteros")
pc()