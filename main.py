# main.py : programme principal de la playlist de party

# TODO 1 : importer le module playlist
import playlist


# TODO 2 : créer le dictionnaire vide ma_playlist
#          et les listes titres et durees (5 éléments chacune)
ma_playlist = {
}

titres = ["Music 1", "Music 2", "Music 3", "Music 4", "Music 5"]
durees = [260, 210, 300, 150, 120]

# TODO 3 : avec une boucle for et range(len(titres)),
#          ajouter chaque chanson à ma_playlist
for i in range(len(titres)):
    playlist.ajouter_chanson(ma_playlist, titres[i], durees[i])


# TODO 4 : afficher chaque chanson avec sa durée formatée
#          (ex. : Nuit blanche - 3:05)
for key, value in ma_playlist.items():
    print(f"{key} - {playlist.formater_duree(value):>5}s")


# TODO 5 : afficher la durée totale de la playlist, formatée
total = playlist.duree_totale(ma_playlist)
print(f"La playlist a une durée de {playlist.formater_duree(total)}.")

# TODO 6 : afficher la chanson la plus longue
plus_longue = playlist.chanson_la_plus_longue(ma_playlist)
print(f"La chanson la plus longue est {plus_longue}")

# TODO 7 : demander une durée maximale en secondes (input, converti en int),
#          puis afficher la liste des chansons plus courtes que cette durée
max_sec = int(input("Veuillez entrer la durée maximale: "))
courtes = playlist.chansons_courtes(ma_playlist, max_sec)
for titre in courtes:
    print(f"Les chansons courtes sont:\n{titre}")

# TODO 8 : demander le titre d'une chanson à retirer
#          - si elle est absente : afficher un message
#          - sinon : la retirer et réafficher la playlist
chanson_retirer = input("Veuillez entrer le titre d'une chanson que vous désirez retirer: ")
for key, value in ma_playlist.items:
    if chanson_retirer not in list(ma_playlist):
        print("Titre non retrouvé!")
    elif chanson_retirer == key:
        playlist.retirer_chanson(ma_playlist, key)

# TODO 9 : tester votre programme, corriger les erreurs d'exécutions et de logique
#          incluant celles dans le module.

# TODO 10 : tester avec des valeurs incorrectes, exemple un titre qui n'existe pas,
#           une durée en str, et ajouter la gestion d'exceptions, incluant dans le module.