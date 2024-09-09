""" Le module math fourni la fonction racine carré. """
from math import sqrt


#### Fonction secondaire


def isprime(p:int)->bool:
    """
    Objectif : la fonction cherche à déterminer si p est un nombre premier.

    Argument : un nombre quelconque.

    Retourne : un booléen qui est True si p est premier et False sinon.
    """

    a=int(sqrt(p)) # On assigne la variable a à la racine carré de p.

    if p in (0,1) : # Cas spécifiques de 0 et 1.
        return False

    for i in range (2,a+1): # On essaie pour tous les nombres entre 2 et racine de p.
        if p%i==0: # On cherche à savoir si le reste de la division entre p et i est nul.
            return False # p n'est pas premier.
    return True # p est premier.


#### Fonction principale


def main():
    """
    Renvoi les nombres premiers qui sont dans les 100 premiers nombres entiers (0,1,2,3,...,98,99).
    """
    for n in range(100):
        if isprime(n) is True: # On vérifie si le nombre est premier avec la fonction isprime.
            print(n, end=", ")

    print()

if __name__ == "__main__":
    main()
