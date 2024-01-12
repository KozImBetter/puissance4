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
    if next((wrong for line in plateau for c in line if not (c is None) and not type_pion(c)), True) == wrong:
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
    :raise TypeError: - Si le plateau n'est pas valide
                      - Si le pion n'est pas valide
                      - Si la colonne n'est pas un entier
    :raise ValueError: Si la colonne n'existe pas
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
    print(('-' * len(plateau[0]) * 2) + '-')

    for i in range(0, len(plateau[0])):
        print(f' {i}', end="")
    print("\n")

    return None


def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de 4 pions qui s'enchaines sur chaque ligne
    :param plateau: Tableau 2D correspondant à un plateau
    :param couleur: Entier réprésentant la couleur rouge (1) ou jaune (2)
    :return: liste des pions qui s'enchaines à 4 ou plus sur chaque ligne
    :raise TypeError: - Si le plateau n'est pas valide
                      - Si la couleur n'est pas un entier
    :raise ValueError: Si la couleur n'est pas valide
    """
    if len(plateau) != const.NB_LINES and len(plateau[0]) != const.NB_COLMUNS:
        raise TypeError('detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau')
    if type(couleur) is not int:
        raise TypeError('detecter4horizontalPlateau : le second paramètre n’est pas un entier')
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f'détecter4horizontalPlateau : La valeur de la couleur ({couleur}) n’est pas correcte ')

    L_aligne = []
    for i in range(0, len(plateau)):
        L_temp = []
        L_test = []
        for j in range(0, len(plateau[i])):

            if type(plateau[i][j]) is dict:
                if (plateau[i][j]).get(const.COULEUR) == couleur:
                    L_temp.append(plateau[i][j])
                    L_test.append(j)

        suivi = 0

        for test in range(0, len(L_temp) - 1):
            if L_test[test] + 1 == L_test[test + 1]:
                suivi += 1
            else:
                suivi = 0
                L_temp[test] = None

            if suivi == 3:
                L_aligne = L_aligne + L_temp[:4].copy()

    return L_aligne


def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de 4 pions qui s'enchaines sur chaque colonnes
    :param plateau: Tableau 2D correspondant à un plateau
    :param couleur: Entier réprésentant la couleur rouge (1) ou jaune (2)
    :return: liste des pions qui s'enchaines à 4 ou plus sur chaque colonnes
    :raise TypeError: - Si le plateau n'est pas valide
                      - Si la couleur n'est pas un entier
    :raise ValueError: Si la couleur n'est pas valide
    """
    if len(plateau) != const.NB_LINES and len(plateau[0]) != const.NB_COLMUNS:
        raise TypeError('detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau')
    if type(couleur) is not int:
        raise TypeError('detecter4verticalPlateau : le second paramètre n’est pas un entier')
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f'detecter4verticalPlateau : La valeur de la couleur ({couleur}) n’est pas correcte ')

    L_aligne = []
    for j in range(len(plateau[0])):
        L_temp = []
        L_test = []
        for i in range(len(plateau)):

            if type(plateau[i][j]) is dict:
                if (plateau[i][j]).get(const.COULEUR) == couleur:
                    L_temp.append(plateau[i][j])
                    L_test.append(i)

        suivi = 0

        for test in range(len(L_temp) - 1):
            if L_test[test] + 1 == L_test[test + 1]:
                suivi += 1
            else:
                suivi = 0
                L_temp[test] = None

            if suivi == 3:
                L_aligne = L_aligne + L_temp[:4].copy()

    return L_aligne


def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de 4 pions qui s'enchaines sur chaque diagonales directes
    :param plateau: Tableau 2D correspondant à un plateau
    :param couleur: Entier réprésentant la couleur rouge (1) ou jaune (2)
    :return: liste des pions qui s'enchaines à 4 ou plus sur chaque diagonales directes, liste vide sinon
    :raise TypeError: - Si le plateau n'est pas valide
                      - Si la couleur n'est pas un entier
    :raise ValueError: Si la couleur n'est pas valide
    """
    if len(plateau) != const.NB_LINES and len(plateau[0]) != const.NB_COLMUNS:
        raise TypeError('detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau')
    if type(couleur) is not int:
        raise TypeError('detecter4diagonaleDirectePlateau : le second paramètre n’est pas un entier')
    if couleur != const.ROUGE and couleur != const.JAUNE:
        raise ValueError(f'detecter4diagonaleDirectePlateau : La valeur de la couleur ({couleur}) n’est pas correcte ')

    L_aligne = []
    for i in range(len(plateau) - 3):
        for j in range(len(plateau[i]) - 3):
            pions_diagonale = [plateau[i + k][j + k] for k in range(4)]

            if all(type(p) is dict and p.get(const.COULEUR) == couleur for p in pions_diagonale):
                L_aligne.append(pions_diagonale)

    return L_aligne