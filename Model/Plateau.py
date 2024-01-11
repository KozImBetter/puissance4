from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau() -> list:
    """
    Construit un tableau 2D correspondant à un plateau

    :return: Renvoie tableau 2D
    """
    temp = []
    plateau = []
    for i in range(0, const.NB_COLUMNS):
        temp.append(None)
    for j in range(0, const.NB_LINES):
        plateau.append(temp.copy())
    return plateau


def placerPionPlateau(plateau: list, pion: dict, col: int) -> int:
    """
    Renvoie la ligne où doit se situer le pion après l'avoir posé, renvoie -1 si la colonne est pleine

    :param plateau: Tableau 2D correspondant à un plateau
    :param pion: Dictionnaire représentant le pion
    :param col: Colonne où l'on souhaite poser le pion
    :return: Renvoie la ligne du pion après l'avoir posé, renvoie -1 si la colonne est pleine
    """
    if len(plateau) != const.NB_LINES and len(plateau[0]) != const.NB_COLMUNS:
        raise TypeError('placerPionPlateau : Le premier paramètre ne correspond pas à un plateau')
    if type(pion) is not dict or len(pion) != 2:
        raise TypeError("setIdPion : Le paramètre n’est pas un pion")
    elif const.COULEUR not in pion.keys() or const.ID not in pion.keys():
        raise TypeError("setIdPion : Le paramètre n’est pas un pion")
    if type(col) is not int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier")
    if col < 0 or col > const.NB_COLUMNS - 1:
        raise ValueError(f"La valeur de la colonne ({col}) n’est pas correcte ")

    ligne = 0
    flag = True

    if plateau[ligne][col] is not None:
        ligne = -1
    else:
        while ligne < const.NB_LINES - 1 and flag:
            ligne += 1

            if plateau[ligne][col] is not None:
                flag = False

        if plateau[ligne][col] is not None:
            ligne -= 1

        plateau[ligne][col] = pion
    return ligne


def toStringPlateau(plateau: list) -> None:
    """
    Fonction permettant d'afficher le plateau

    :param plateau: Tableau 2D correspondant à un plateau
    :return: Ne renvoie rien
    """
    for i in range(0, len(plateau)):
        for j in range(0, len(plateau[i])):

            print('|', end='')
            if type(plateau[i][j]) is not dict:
                print(' ', end='')

            elif (plateau[i][j]).get(const.COULEUR) == const.ROUGE:
                print("\x1B[41m \x1B[0m", end='')

            else:
                print("\x1B[43m \x1B[0m", end='')

        print('|')
    print(('-'*len(plateau[0])*2) + '-')

    for i in range(0,len(plateau[0])):
        print(f' {i}', end="")
    print("\n")

    return None