import random

from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def construireJoueur(couleur: int) -> dict:
    """
    Consuitruit un dictionnaire représentant le joueur

    :param couleur: Entier réprésentant la couleur rouge (1) ou jaune (2)
    :return: Renvoie un dictionnaire qui représente le joueur
    """
    if type(couleur) is not int:
        raise TypeError("construireJoueur : Le paramètre n’est pas un entier")
    if couleur not in (const.ROUGE, const.JAUNE):
        raise ValueError(f"construireJoueur : L’entier donné ({couleur}) n’est pas une couleur")
    return {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}


def getCouleurJoueur(joueur: dict) -> int:
    """
    Renvoie la couleur d'un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Renvoie  un entier réprésentant la couleur rouge (1) ou jaune (2)
    :raise TypeError: Si le pramamètre n'est pas un joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.COULEUR]


def getPlateauJoueur(joueur: dict) -> list:
    """
    Renvoie le plateau d'un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Renvoie  liste 2D réprésentant le plateau du joueur
    :raise TypeError: Si le pramamètre n'est pas un joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLATEAU]


def getPlacerPionJoueur(joueur: dict) -> 'function':
    """
    Renvoie la fonction d'un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Renvoie la fonction du joueur
    :raise TypeError: Si le pramamètre n'est pas un joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]


def getPionJoueur(joueur: dict) -> dict:
    """
    Construit un pion pour un joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Pion à la couleur du joueur
    :raise TypeError: Si le pramamètre n'est pas un joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    return construirePion(getCouleurJoueur(joueur))


def setPlateauJoueur(joueur: dict, plateau: dict) -> None:
    """
    Associe un plateau à un joueur

    :param joueur: Dictionnaire représentant le joueur
    :param plateau: Liste 2D réprésentant un plateau
    :return: Rien
    :raise TypeError: - Si le premier paramètre n'est pas un joueur
                      - Si le second paramètre n'est pas un plateau
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur ")
    if not type_plateau(plateau):
        raise TypeError("« setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None


def setPlacerPionJoueur(joueur: dict, fn: callable) -> None:
    """
    Associe une fonction à un joueur

    :param joueur: Dictionnaire représentant le joueur
    :param fn: Fonction déternimant l'action du joueur
    :return: Rien
    :raise TypeError: - Si le premier paramètre n'est pas un joueur
                      - Si le second paramètre n'est pas une fonction
    """
    if not type_joueur(joueur):
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if not callable(fn):
        raise TypeError("setPlacerPionJoueur : le second paramètre n’est pas une fonction")
    joueur[const.PLACER_PION] = fn
    return None


def _placerPionJoueur(joueur: dict) -> int:
    """
    Choisis aléatoirement où placer un pion un tableau

    :param joueur: Dictionnaire représentant le joueur
    :return: Indice de la colonne où poser le pion
    """
    col = None
    L = []
    for i in range(0, const.NB_COLUMNS):
        L.append(i)
    while col == None:
        potentiel = random.randint(0, len(L)-1)
        if joueur[const.PLATEAU][0][potentiel] is None:
            col = potentiel
        else:
            L.pop(potentiel)
    return col


def initialiserIAJoueur(joueur: dict, ordre: bool) -> None:
    """
    Permet le fonctionnemment de l'IA stupide

    :param joueur:
    :param ordre: Orde de passage, True (1er) ou False(2ème)
    :return: Rien
    :raise TypeError: - Si le premier paramètre n'est pas joueur
                      - Si le deuxième paramètre n'est pas un booléen
    """
    if not type_joueur(joueur):
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueur")
    if type(ordre) is not bool:
        raise TypeError("initialiserIAJoueur: Le second paramètre n’est pas un booléen")
    joueur[const.PLACER_PION] = _placerPionJoueur
    return None
