"""
Ce module permet de rechercher des mots dans un dictionnaire, en utilisant des caractères génériques (wildcards).

**Fonctionnement général:**

1. **Chargement du dictionnaire:** Le module charge un dictionnaire de mots depuis un fichier texte.
2. **Recherche de mots:** L'utilisateur saisit un mot à rechercher, qui peut contenir des caractères génériques (représentés par le caractère '?'). 
3. **Affichage des résultats:** Le module affiche tous les mots du dictionnaire qui correspondent au motif de recherche.

**Exemple d'utilisation:**

Pour rechercher tous les mots de 4 lettres commençant par 'C' et se terminant par 'T', vous pouvez saisir le motif "C??T".

**Note:** Les mots du dictionnaire sont automatiquement convertis en majuscules pour les recherches.

**Modules utilisés:**

* `re`: Module pour l'utilisation d'expressions régulières, permettant la recherche de motifs avec des caractères génériques.

**Limitations:**

* Les caractères génériques ne peuvent représenter qu'une seule lettre.
* Le dictionnaire est chargé en mémoire, ce qui peut limiter la taille des dictionnaires utilisables.

"""

import re
import os

def create_dictionary():
    """
    Crée un dictionnaire indexé par le nombre de lettres, en majuscules et sans doublons.

    Returns:
        dict: Un dictionnaire où les clés sont des nombres représentant la longueur des mots,
              et les valeurs sont des ensembles de mots de cette longueur.
    """
    print('Chargement du dictionnaire ...')
    words_count=0
    dictionary = {}
    dir_path=os.path.dirname(os.path.realpath(__file__))
    dictionary_path=os.path.join(dir_path,'data','dico.txt')
    with open(dictionary_path, "r") as f:
        for line in f:
            word = line.strip().upper()  # Convertit en majuscules et supprime les espaces
            length = len(word)
            dictionary.setdefault(length, set()).add(word)  # Utilise un set pour éviter les doublons
            words_count+=1
    print(f'{words_count} mots chargés')
    return dictionary

def find_words(dictionary, pattern):
    """
    Trouve les mots correspondant au pattern dans le dictionnaire.

    Args:
        dictionary (dict): Le dictionnaire de mots.
        pattern (str): Le pattern de recherche avec des wildcards (?).

    Returns:
        list: Une liste de mots correspondant au pattern.
    """
    regex = pattern.strip().upper().replace('?', '.')
    length = len(regex)
    if length in dictionary:
        return [word for word in dictionary[length] if re.match(regex, word)]
    else:
        return []

def run():
    """
    Point d'entrée principal de l'application.

    Il permet de :

    * Charger le dictionnaire de mots.
    * Effectuer des recherches de mots avec des wildcards.
    * Afficher les résultats à l'utilisateur.
    """
    dictionary=create_dictionary()
    while True:
        proposal = input("Entrez votre mot avec ? pour les lettres manquantes, ou 'q' pour quitter \n mot : ")
        if proposal == 'q':
            break
        submissions=find_words(dictionary,proposal)
        if len(submissions)>0:
            for submission in submissions:
                print(submission)
        else:
            print('Il n\'y a pas de mots correspondants dans le dictionnaire')

if __name__ == "__main__":
    run()
