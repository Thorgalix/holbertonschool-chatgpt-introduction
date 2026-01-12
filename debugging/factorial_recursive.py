#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un entier donné de manière récursive.

    Description :
        La fonction factorial calcule le produit de tous les entiers positifs 
        inférieurs ou égaux à n. La factorielle de 0 est définie comme 1. 
        La fonction utilise la récursion pour effectuer le calcul.

    Paramètres :
        n (int) : L'entier dont on souhaite calculer la factorielle. 
                  Doit être un entier >= 0.

    Retour :
        int : La factorielle de l'entier n.
               - Si n = 0, retourne 1.
               - Si n > 0, retourne n * factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupération de l'argument passé en ligne de commande
f = factorial(int(sys.argv[1]))

# Affichage du résultat
print(f)
