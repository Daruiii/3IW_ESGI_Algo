#!/usr/bin/env python3
"""
Fonctions utilitaires pour le projet d'analyse de performance
- Lecture du CSV sans bibliothèque externe
- Mesure de temps et comptage d'opérations
- Affichage et sauvegarde des résultats
"""

import time

def lire_csv(nom_fichier):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires
    Format attendu : date_mutation,prix,surface,commune,type_local,nb_pieces,code_postal,prix_m2
    
    Args:
        nom_fichier (str): Nom du fichier CSV à lire
        
    Returns:
        list: Liste de dictionnaires contenant les données
    """
    donnees = []
    
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
            
            # Première ligne = en-têtes
            if len(lignes) > 0:
                entetes = lignes[0].strip().split(',')
                
                # Traiter chaque ligne de données
                for ligne in lignes[1:]:
                    valeurs = ligne.strip().split(',')
                    
                    if len(valeurs) == len(entetes):
                        # Créer un dictionnaire pour chaque ligne
                        enregistrement = {}
                        for i, entete in enumerate(entetes):
                            if entete in ['prix', 'surface', 'nb_pieces', 'code_postal', 'prix_m2']:
                                # Convertir en entier pour les colonnes numériques
                                try:
                                    enregistrement[entete] = int(valeurs[i])
                                except ValueError:
                                    enregistrement[entete] = 0
                            else:
                                enregistrement[entete] = valeurs[i]
                        
                        donnees.append(enregistrement)
                        
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []
    
    return donnees

def extraire_colonne(donnees, nom_colonne):
    """
    Extrait une colonne spécifique des données
    
    Args:
        donnees (list): Liste de dictionnaires
        nom_colonne (str): Nom de la colonne à extraire
        
    Returns:
        list: Liste des valeurs de la colonne
    """
    return [enregistrement[nom_colonne] for enregistrement in donnees if nom_colonne in enregistrement]

def mesurer_temps(fonction, *args, **kwargs):
    """
    Mesure le temps d'exécution d'une fonction
    
    Args:
        fonction: Fonction à mesurer
        *args: Arguments positionnels de la fonction
        **kwargs: Arguments nommés de la fonction
        
    Returns:
        tuple: (résultat_fonction, temps_execution)
    """
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    temps_execution = fin - debut
    
    return resultat, temps_execution

def afficher_resultats_tri(nom_algo, critere, taille, temps, nb_comparaisons, nb_operations=None):
    """
    Affiche les résultats d'un test de tri selon le format demandé
    
    Args:
        nom_algo (str): Nom de l'algorithme
        critere (str): Critère de tri (PRIX, SURFACE)
        taille (int): Taille du tableau
        temps (float): Temps d'exécution
        nb_comparaisons (int): Nombre de comparaisons
        nb_operations (int): Nombre d'opérations (échanges, décalages)
    """
    if nb_operations is not None:
        if nom_algo == "INSERTION":
            print(f"Tri {nom_algo} par {critere} : {temps:.4f}s | {nb_comparaisons} comparaisons | {nb_operations} décalages")
        else:
            print(f"Tri {nom_algo} par {critere} : {temps:.4f}s | {nb_comparaisons} comparaisons | {nb_operations} échanges")
    else:
        print(f"Tri {nom_algo} par {critere} : {temps:.4f}s | {nb_comparaisons} comparaisons")

def afficher_resultats_recherche(nom_algo, critere, temps, nb_comparaisons, resultat_specifique=""):
    """
    Affiche les résultats d'un test de recherche selon le format demandé
    
    Args:
        nom_algo (str): Nom de l'algorithme de recherche
        critere (str): Critère de recherche
        temps (float): Temps d'exécution
        nb_comparaisons (int): Nombre de comparaisons
        resultat_specifique (str): Résultat spécifique (position, min/max, etc.)
    """
    print(f"{nom_algo} {critere} : {temps:.4f}s | {nb_comparaisons} comparaisons{resultat_specifique}")

def sauvegarder_resultats(nom_fichier, contenu):
    """
    Sauvegarde les résultats dans un fichier
    
    Args:
        nom_fichier (str): Nom du fichier de sauvegarde
        contenu (str): Contenu à sauvegarder
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            fichier.write(contenu)
        print(f"Résultats sauvegardés dans {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def copier_liste(liste):
    """
    Crée une copie d'une liste (pour éviter de modifier l'original)
    
    Args:
        liste (list): Liste à copier
        
    Returns:
        list: Copie de la liste
    """
    return liste.copy()
