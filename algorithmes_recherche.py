#!/usr/bin/env python3
"""
Implémentation des 3 algorithmes de recherche obligatoires
- Recherche Linéaire
- Recherche Binaire
- Recherche Min/Max

Chaque algorithme retourne : (résultat, nb_comparaisons, temps_execution)
"""

import time

def recherche_lineaire(tableau, valeur_cible):
    """
    Recherche Linéaire : Parcourir le tableau de gauche à droite jusqu'à trouver l'élément
    
    Args:
        tableau (list): Tableau dans lequel rechercher
        valeur_cible: Valeur à rechercher
        
    Returns:
        tuple: (position_trouvee, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    nb_comparaisons = 0
    position_trouvee = -1
    
    for i in range(len(tableau)):
        nb_comparaisons += 1
        if tableau[i] == valeur_cible:
            position_trouvee = i
            break
    
    fin = time.time()
    temps_execution = fin - debut
    
    return position_trouvee, nb_comparaisons, temps_execution

def recherche_lineaire_multiple(donnees, critere_fonction):
    """
    Recherche Linéaire pour compter toutes les occurrences répondant à un critère
    
    Args:
        donnees (list): Liste de dictionnaires à parcourir
        critere_fonction: Fonction qui prend un enregistrement et retourne True/False
        
    Returns:
        tuple: (nombre_trouve, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    nb_comparaisons = 0
    nombre_trouve = 0
    
    for enregistrement in donnees:
        nb_comparaisons += 1
        if critere_fonction(enregistrement):
            nombre_trouve += 1
    
    fin = time.time()
    temps_execution = fin - debut
    
    return nombre_trouve, nb_comparaisons, temps_execution

def recherche_binaire(tableau_trie, valeur_cible):
    """
    Recherche Binaire : Dans un tableau trié, diviser par 2 à chaque étape selon la comparaison
    
    Args:
        tableau_trie (list): Tableau trié dans lequel rechercher
        valeur_cible: Valeur à rechercher
        
    Returns:
        tuple: (position_trouvee, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    nb_comparaisons = 0
    position_trouvee = -1
    
    gauche = 0
    droite = len(tableau_trie) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        nb_comparaisons += 1
        
        if tableau_trie[milieu] == valeur_cible:
            position_trouvee = milieu
            break
        elif tableau_trie[milieu] < valeur_cible:
            nb_comparaisons += 1  # Comparaison supplémentaire pour <
            gauche = milieu + 1
        else:
            nb_comparaisons += 1  # Comparaison supplémentaire pour >
            droite = milieu - 1
    
    fin = time.time()
    temps_execution = fin - debut
    
    return position_trouvee, nb_comparaisons, temps_execution

def recherche_min_max(tableau):
    """
    Recherche Min/Max : Trouver la valeur minimale ET maximale en un seul parcours
    
    Args:
        tableau (list): Tableau dans lequel chercher min et max
        
    Returns:
        tuple: (valeur_min, valeur_max, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    if len(tableau) == 0:
        fin = time.time()
        return None, None, 0, fin - debut
    
    nb_comparaisons = 0
    valeur_min = tableau[0]
    valeur_max = tableau[0]
    
    for i in range(1, len(tableau)):
        nb_comparaisons += 1
        if tableau[i] < valeur_min:
            valeur_min = tableau[i]
        
        nb_comparaisons += 1
        if tableau[i] > valeur_max:
            valeur_max = tableau[i]
    
    fin = time.time()
    temps_execution = fin - debut
    
    return valeur_min, valeur_max, nb_comparaisons, temps_execution

def recherche_min_max_optimisee(tableau):
    """
    Recherche Min/Max optimisée : Comparer par paires pour réduire le nombre de comparaisons
    
    Args:
        tableau (list): Tableau dans lequel chercher min et max
        
    Returns:
        tuple: (valeur_min, valeur_max, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    if len(tableau) == 0:
        fin = time.time()
        return None, None, 0, fin - debut
    
    nb_comparaisons = 0
    
    # Initialiser min et max
    if len(tableau) % 2 == 0:
        # Nombre pair d'éléments
        nb_comparaisons += 1
        if tableau[0] < tableau[1]:
            valeur_min = tableau[0]
            valeur_max = tableau[1]
        else:
            valeur_min = tableau[1]
            valeur_max = tableau[0]
        start_idx = 2
    else:
        # Nombre impair d'éléments
        valeur_min = tableau[0]
        valeur_max = tableau[0]
        start_idx = 1
    
    # Traiter les éléments par paires
    for i in range(start_idx, len(tableau), 2):
        if i + 1 < len(tableau):
            # Comparer les deux éléments de la paire
            nb_comparaisons += 1
            if tableau[i] < tableau[i + 1]:
                petit = tableau[i]
                grand = tableau[i + 1]
            else:
                petit = tableau[i + 1]
                grand = tableau[i]
            
            # Comparer avec min et max actuels
            nb_comparaisons += 1
            if petit < valeur_min:
                valeur_min = petit
            
            nb_comparaisons += 1
            if grand > valeur_max:
                valeur_max = grand
        else:
            # Élément seul (si nombre impair)
            nb_comparaisons += 1
            if tableau[i] < valeur_min:
                valeur_min = tableau[i]
            
            nb_comparaisons += 1
            if tableau[i] > valeur_max:
                valeur_max = tableau[i]
    
    fin = time.time()
    temps_execution = fin - debut
    
    return valeur_min, valeur_max, nb_comparaisons, temps_execution

# Fonctions helper pour les critères de recherche spécifiques au projet

def critere_maisons_paris(enregistrement):
    """
    Critère pour rechercher les maisons à Paris
    
    Args:
        enregistrement (dict): Un enregistrement du CSV
        
    Returns:
        bool: True si c'est une maison à Paris
    """
    return (enregistrement.get('type_local') == 'Maison' and 
            enregistrement.get('commune') == 'PARIS')

def critere_appartements_3_pieces(enregistrement):
    """
    Critère pour rechercher les appartements 3 pièces
    
    Args:
        enregistrement (dict): Un enregistrement du CSV
        
    Returns:
        bool: True si c'est un appartement 3 pièces
    """
    return (enregistrement.get('type_local') == 'Appartement' and 
            enregistrement.get('nb_pieces') == 3)

def tester_recherche(fonction_recherche, *args, nom_algo=""):
    """
    Fonction helper pour tester un algorithme de recherche
    
    Args:
        fonction_recherche: Fonction de recherche à tester
        *args: Arguments pour la fonction de recherche
        nom_algo (str): Nom de l'algorithme pour l'affichage
        
    Returns:
        tuple: Résultats de la recherche
    """
    if nom_algo:
        print(f"Test de {nom_algo}...")
    return fonction_recherche(*args)
