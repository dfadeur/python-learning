# /usr/bin/python3
# -*-coding:utf-8 -*

from multiplication import *

nombre = input("nombre : ")

try:
    nombre = int(nombre)
except:
    print("vous n'avez pas entré un nombre correct")
else:
    limite = input("limite : ")
    try:
        limite = int(limite)
    except:
        print("vous n'avez pas entré une limite correcte")
    else:
        multiplication(nombre, limite)


