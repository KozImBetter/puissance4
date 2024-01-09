# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(color: int) -> dict:
    """
     Cette fonction reçoit une couleur en paramètre et retourne
     un pion construit avec cette couleur

    :param color: Couleur du pion à construire
    :return: Dictionnaire représentant le pion
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type(color) is not int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")

    if color not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur ({color}) n’est pas correcte")

    pion = {const.COULEUR: const.COULEURS[color], const.ID: None}
    return pion


def getCouleurPion(pion: dict) -> int:
    """
    Cette fonction retourne la couleur du pion passé en paramètre

    :param pion: Dictionnaire représentant le pion
    :return: Couleur du pion
    :raise TypeError: Si le dictionnaire ne représente pas un pion
    """

    if not type(pion) is dict or len(pion) != 2:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion")
    elif const.COULEUR not in pion.keys() or const.ID not in pion.keys():
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion")
    return pion[const.COULEUR]


def setCouleurPion(pion: dict, color: int) -> None:
    """
    Cette fonction modifie la couleur du pion passé en premier
    paramètre avec la nouvelle couleur passée en second paramètre

    :param pion: Dictionnaire représentant le pion
    :param color: Nouvelle couleur du pion
    :return: Rien
    :raise TypeError: - Si le dictionnaire ne représente pas un pion
                      - Si l'entier ne représente pas une couleur
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(pion) is not dict or len(pion) != 2:
        raise TypeError("setCouleurPion : Le paramètre n’est pas un pion")
    elif const.COULEUR not in pion.keys() or const.ID not in pion.keys():
        raise TypeError("setCouleurPion : Le paramètre n’est pas un pion")

    if type(color) is not int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")

    if color not in const.COULEURS:
        raise ValueError(f"setCouleurPion : la couleur ({color}) n’est pas correcte")

    pion[const.COULEUR] = const.COULEURS[color]
    return None


