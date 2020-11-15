import donnees
import fonctions

nom = fonctions.saisie_nom_joueur()

score = fonctions.read_score(nom, donnees.socres_file)
print("Votre score actuel est de : ", score)

jouer_encore = True

while jouer_encore:

    content = fonctions.lire_mot_a_deviner()
    random_word = fonctions.get_random_word(content)
    # print(random_word)
    tentative_restantes = donnees.max_tentatives
    mot_non_trouve = True

    caracteres_saisies = list()

    while tentative_restantes > 0 and mot_non_trouve:
        print(fonctions.print_hided_word(random_word, caracteres_saisies))
        caracteres_saisies += fonctions.saisie_char()
        hided_word = fonctions.print_hided_word(random_word, caracteres_saisies)
        if "*" in hided_word:
            mot_non_trouve = True
        else:
            mot_non_trouve = False

        # calculer le nombre de tentatives restantes
        tentatives_rate = fonctions.get_tentatives_restants(random_word, caracteres_saisies)
        tentative_restantes = donnees.max_tentatives - tentatives_rate
        print(str.format("Il vous reste {0} tentatives", tentative_restantes))

    print("Votre score de cette partie est : ", tentative_restantes)
    score += tentative_restantes
    print("Votre score total est de : ", score)
    fonctions.add_score(nom, score, donnees.socres_file)

    jouer_encore = fonctions.saisie_end_game()

print("Vous avez terminé la partie avec un score total de : ", score)
