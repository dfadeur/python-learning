# /usr/bin/python3
# -*-coding:utf-8 -*
import os


def multiplication(nb, limite):

    i = 0  # C'est notre variable compteur que nous allons incrémenter dans la boucle

    while i < limite:  # Tant que i est strictement inférieure à 10
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1  # On incrémente i de 1 à chaque tour de boucle

# test de la fonction multiplication


if __name__ == "__main__":
    multiplication(4, 5)
    os.system("pause")
