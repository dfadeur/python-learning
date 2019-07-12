# /usr/bin/python3
# -*-coding:utf-8 -*

from random import randrange
from math import ceil

money = 10

while money > 0:
    nombre = input("nombre : ")
    gain = 0
    try:
        nombre = int(nombre)
        if nombre < 0 or nombre > 49:
            raise ValueError("Nombre doit être compris entre 0 et 49.")
    except ValueError:
        print("vous n'avez pas entré un nombre correct")
    mise = input("mise : ")

    try:
        mise = int(mise)
        if mise < 0 or mise > money:
            raise ValueError("Mise doit être compris entre 1 et ", money, "€.")
    except ValueError:
        print("vous n'avez pas entré une mise correcte (entre 1 et ", money, "€.")
    else:
        money -= mise

    if not nombre % 2:
        couleur = "Noir"
    else:
        couleur="Rouge"

    print("Vous misez ", mise, "€ sur le ", nombre, "(", couleur, ")")

    tirage = (randrange(49))

    if not tirage % 2:
        couleur_tirage = "Noir"
    else:
        couleur_tirage="Rouge"
    print("Le gagnant est le ", tirage, ", ", couleur_tirage)

    if nombre == tirage:
        gain = 3 * mise
    elif couleur == couleur_tirage:
        gain = ceil(mise / 2)
    money += gain
    print("Vous gagnez ", gain, "€. Votre magot est de ", money, "€.")

