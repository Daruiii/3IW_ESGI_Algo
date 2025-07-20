#!/usr/bin/env python3
"""
Programme principal pour l'analyse de performance d'algorithmes
Tri et Recherche sur des données immobilières
"""

import time
from utilitaires import (
    lire_csv, extraire_colonne, afficher_resultats_tri, afficher_resultats_recherche,
    sauvegarder_resultats, copier_liste
)
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import (
    recherche_lineaire, recherche_binaire, recherche_min_max,
    recherche_lineaire_multiple, critere_maisons_paris, critere_appartements_3_pieces
)

def tester_tris(donnees, taille):
    """
    Teste tous les algorithmes de tri sur les données
    
    Args:
        donnees (list): Données complètes
        taille (int): Nombre d'éléments à tester
        
    Returns:
        str: Résultats formatés pour sauvegarde
    """
    # Prendre seulement les premiers éléments
    donnees_test = donnees[:taille]
    
    # Extraire les colonnes pour les tests
    prix = extraire_colonne(donnees_test, 'prix')
    surface = extraire_colonne(donnees_test, 'surface')
    
    resultats_texte = []
    
    # Tests de tri par PRIX
    print(f"\n=== TRI PAR PRIX ({taille} éléments) ===")
    resultats_texte.append(f"\n=== TRI PAR PRIX ({taille} éléments) ===")
    
    # Tri par sélection
    arr_trie, nb_comp, nb_ech, temps = tri_selection(prix)
    afficher_resultats_tri("SÉLECTION", "PRIX", taille, temps, nb_comp, nb_ech)
    resultats_texte.append(f"Tri SÉLECTION par PRIX : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Tri par insertion
    arr_trie, nb_comp, nb_dec, temps = tri_insertion(prix)
    afficher_resultats_tri("INSERTION", "PRIX", taille, temps, nb_comp, nb_dec)
    resultats_texte.append(f"Tri INSERTION par PRIX : {temps:.4f}s | {nb_comp} comparaisons | {nb_dec} décalages")
    
    # Tri fusion
    arr_trie, nb_comp, temps = tri_fusion(prix)
    afficher_resultats_tri("FUSION", "PRIX", taille, temps, nb_comp)
    resultats_texte.append(f"Tri FUSION par PRIX : {temps:.4f}s | {nb_comp} comparaisons")
    
    # Tri rapide
    arr_trie, nb_comp, nb_ech, temps = tri_rapide(prix)
    afficher_resultats_tri("RAPIDE", "PRIX", taille, temps, nb_comp, nb_ech)
    resultats_texte.append(f"Tri RAPIDE par PRIX : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Tests de tri par SURFACE
    print(f"\n=== TRI PAR SURFACE ({taille} éléments) ===")
    resultats_texte.append(f"\n=== TRI PAR SURFACE ({taille} éléments) ===")
    
    # Tri par sélection
    arr_trie, nb_comp, nb_ech, temps = tri_selection(surface)
    afficher_resultats_tri("SÉLECTION", "SURFACE", taille, temps, nb_comp, nb_ech)
    resultats_texte.append(f"Tri SÉLECTION par SURFACE : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Tri par insertion
    arr_trie, nb_comp, nb_dec, temps = tri_insertion(surface)
    afficher_resultats_tri("INSERTION", "SURFACE", taille, temps, nb_comp, nb_dec)
    resultats_texte.append(f"Tri INSERTION par SURFACE : {temps:.4f}s | {nb_comp} comparaisons | {nb_dec} décalages")
    
    # Tri fusion
    arr_trie, nb_comp, temps = tri_fusion(surface)
    afficher_resultats_tri("FUSION", "SURFACE", taille, temps, nb_comp)
    resultats_texte.append(f"Tri FUSION par SURFACE : {temps:.4f}s | {nb_comp} comparaisons")
    
    # Tri rapide
    arr_trie, nb_comp, nb_ech, temps = tri_rapide(surface)
    afficher_resultats_tri("RAPIDE", "SURFACE", taille, temps, nb_comp, nb_ech)
    resultats_texte.append(f"Tri RAPIDE par SURFACE : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    return "\n".join(resultats_texte)

def tester_recherches(donnees, taille):
    """
    Teste tous les algorithmes de recherche sur les données
    
    Args:
        donnees (list): Données complètes
        taille (int): Nombre d'éléments à tester
        
    Returns:
        str: Résultats formatés pour sauvegarde
    """
    # Prendre seulement les premiers éléments
    donnees_test = donnees[:taille]
    
    resultats_texte = []
    
    print(f"\n=== RECHERCHES ({taille} éléments) ===")
    resultats_texte.append(f"\n=== RECHERCHES ({taille} éléments) ===")
    
    # Test A - Recherche de TOUTES les Maisons à Paris (500 et 1000 éléments)
    if taille >= 500:
        nombre_trouve, nb_comp, temps = recherche_lineaire_multiple(donnees_test, critere_maisons_paris)
        print(f"Recherche linéaire MAISONS PARIS : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nombre_trouve}")
        resultats_texte.append(f"Recherche linéaire MAISONS PARIS : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nombre_trouve}")
    
    # Test B - Recherche Binaire d'un Prix Cible (500 et 1000 éléments)
    if taille >= 500:
        # D'abord trier les prix
        prix = extraire_colonne(donnees_test, 'prix')
        prix_trie, _, _, _ = tri_rapide(prix)  # Utiliser tri rapide pour trier
        
        # Rechercher 350000€
        position, nb_comp, temps = recherche_binaire(prix_trie, 350000)
        print(f"Recherche binaire PRIX 350000€ : {temps:.4f}s | {nb_comp} comparaisons | Position: {position}")
        resultats_texte.append(f"Recherche binaire PRIX 350000€ : {temps:.4f}s | {nb_comp} comparaisons | Position: {position}")
    
    # Test C - Recherche Min/Max des Prix au m2 (500 et 1000 éléments)
    if taille >= 500:
        prix_m2 = extraire_colonne(donnees_test, 'prix_m2')
        val_min, val_max, nb_comp, temps = recherche_min_max(prix_m2)
        print(f"Min/Max PRIX_M2 : {temps:.4f}s | {nb_comp} comparaisons | Min: {val_min}€/m2 | Max: {val_max}€/m2")
        resultats_texte.append(f"Min/Max PRIX_M2 : {temps:.4f}s | {nb_comp} comparaisons | Min: {val_min}€/m2 | Max: {val_max}€/m2")
    
    # Test D - Recherche de TOUS les Appartements 3 Pièces (500 et 1000 éléments)
    if taille >= 500:
        nombre_trouve, nb_comp, temps = recherche_lineaire_multiple(donnees_test, critere_appartements_3_pieces)
        print(f"Recherche APPART 3P : {temps:.4f}s | {nb_comp} comparaisons | Trouvés: {nombre_trouve}")
        resultats_texte.append(f"Recherche APPART 3P : {temps:.4f}s | {nb_comp} comparaisons | Trouvés: {nombre_trouve}")
    
    return "\n".join(resultats_texte)

def main():
    """
    Programme principal qui lance tous les tests
    """
    print("=== PROJET : ANALYSE DE PERFORMANCE D'ALGORITHMES ===")
    print("Tri et Recherche sur données immobilières")
    print("David - 3IW ESGI")
    print()
    
    # Lecture des données
    print("Lecture des données...")
    donnees = lire_csv("transactions_immobilieres.csv")
    
    if len(donnees) == 0:
        print("Erreur : Impossible de lire les données")
        return
    
    print(f"Données chargées : {len(donnees)} transactions")
    print(f"Colonnes disponibles : {list(donnees[0].keys()) if donnees else 'Aucune'}")
    print()
    
    # Tests sur différentes tailles
    tailles = [100, 500, 1000]
    tous_resultats = []
    
    tous_resultats.append("=== RÉSULTATS DES TESTS D'ALGORITHMES ===")
    tous_resultats.append("Projet : Analyse de Performance d'Algorithmes")
    tous_resultats.append("Tri et Recherche sur données immobilières")
    tous_resultats.append("David - 3IW ESGI")
    tous_resultats.append(f"Date : {time.strftime('%Y-%m-%d %H:%M:%S')}")
    tous_resultats.append(f"Données : {len(donnees)} transactions immobilières")
    tous_resultats.append("\n" + "="*50)
    
    for taille in tailles:
        print(f"\n{'='*50}")
        print(f"TESTS AVEC {taille} ÉLÉMENTS")
        print(f"{'='*50}")
        
        # Tester les tris
        resultats_tri = tester_tris(donnees, taille)
        tous_resultats.append(resultats_tri)
        
        # Tester les recherches
        resultats_recherche = tester_recherches(donnees, taille)
        tous_resultats.append(resultats_recherche)
        
        tous_resultats.append("\n" + "-"*50)
    
    # Sauvegarde des résultats
    contenu_resultats = "\n".join(tous_resultats)
    sauvegarder_resultats("resultats.txt", contenu_resultats)
    
    print(f"\n{'='*50}")
    print("TESTS TERMINÉS !")
    print(f"{'='*50}")
    print("Résultats sauvegardés dans resultats.txt")
    print("\nPour compléter le projet :")
    print("1. Analysez les résultats")
    print("2. Répondez aux questions dans analyse.txt")
    print("3. Préparez votre vidéo avec ScriptVideo.md")
    print()
    
    # Calcul total des tests effectués
    nb_tests_tri = len(tailles) * 4 * 2  # 3 tailles × 4 algos × 2 critères
    nb_tests_recherche = 2 * 4  # 2 tailles (500,1000) × 4 recherches
    print(f"Total des tests effectués : {nb_tests_tri + nb_tests_recherche}")
    print(f"- Tests de tri : {nb_tests_tri}")
    print(f"- Tests de recherche : {nb_tests_recherche}")

if __name__ == "__main__":
    main()
