import os
import pickle
import donnees
import random
import re


def lire_mot_a_deviner():
    with open(donnees.mots_a_deviner, 'r') as file:
        content = file.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    return content


def get_random_word(content: list):
    """
    Renvoie un mot par hasard de la liste d'entrée
    :param content:
    :return:
    """
    return content[random.randrange(len(content))]


def saisie_nom_joueur():
    nom = str()
    while not nom:
        try:
            nom = input("Veuillez saisir votre nom !")
            assert nom, 'Le nom ne doit pas etre vide'
        except AssertionError as erreur:
            print(erreur)
    return nom


def read_score(nom: str, target: str):
    """
    Si le nom du joueur n'existe pas ou si le fichiers des scores est vide la fonction revoie 0 sinon le score
    :param nom:
    :return:
    """
    score_recupere = 0
    if os.path.getsize(target) > 0:
        with open(target, 'rb') as file:
            mon_depickler = pickle.Unpickler(file)
            scores_recuperes = mon_depickler.load()
            if nom in scores_recuperes:
                score_recupere = scores_recuperes[nom]
    return score_recupere


def add_score(nom: str, score: int, target: str):
    if os.path.getsize(target) > 0:
        with open(target, 'rb') as file:
            mon_depickler = pickle.Unpickler(file)
            scores_recuperes = mon_depickler.load()
            scores_recuperes[nom] = score
    else:
        scores_recuperes = dict()
        scores_recuperes[nom] = score

    with open(target, "wb") as file_w:
        mon_depickler_w = pickle.Pickler(file_w)
        mon_depickler_w.dump(scores_recuperes)


def print_hided_word(word: str, caracteres_saisies: list):
    """
    Gérer l'affichage du mot caché en fonction des caractéres trouvés
    :param word:
    :param caracteres_saisies:
    :return:
    """
    output_word = str()
    char_postion = list()
    for char in caracteres_saisies:
        char_postion += [m.start() for m in re.finditer(str.lower(char), str.lower(word))]
    for comp in range(0, len(word)):
        if comp in char_postion:
            output_word += word[comp]
        else:
            output_word += donnees.hide_char

    return output_word


def saisie_char():
    char = str()
    stop_while = True
    while stop_while:
        try:
            char = input("Entrer un caractére qui se trouve dans le mot à trouver: ")
            assert char, 'Le caractére ne doit pas etre vide'
            assert len(char) < 2, 'Veuillez saisir un caractére et non une chaine de caractéres'
            stop_while = False
        except AssertionError as erreur:
            print(erreur)
    return char


def get_tentatives_restants(word: str, caracteres_saisies: list):
    """
    Calculer le nombre de tentatives ratés
    :param word:
    :param caracteres_saisies:
    :return:
    """
    counter = 0
    for letter in caracteres_saisies:
        if str.lower(letter) not in str.lower(word):
            counter += 1
    return counter


def saisie_end_game():
    """
    Saisir la fin du jeu
    :return:
    """
    input_word = str()
    stop_while = True
    while stop_while:
        try:
            input_word = input("Voulez vous continuer de jouer: o/n")
            assert str.lower(input_word) == "o" or str.lower(input_word) == "n", 'saisie non valide'
            stop_while = False
        except AssertionError as erreur:
            print(erreur)
    if str.lower(input_word) == "o":
        return True
    else:
        return False
