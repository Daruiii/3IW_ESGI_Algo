#!/usr/bin/env python3
"""
Implémentation des 4 algorithmes de tri obligatoires
- Tri par Sélection
- Tri par Insertion  
- Tri Fusion
- Tri Rapide

Chaque algorithme retourne : (tableau_trié, nb_comparaisons, nb_operations, temps_execution)
"""

import time

def tri_selection(tableau):
    """
    Tri par Sélection : Trouver le minimum, l'échanger avec le premier élément, répéter
    
    Args:
        tableau (list): Tableau à trier
        
    Returns:
        tuple: (tableau_trié, nb_comparaisons, nb_échanges, temps_execution)
    """
    debut = time.time()
    
    # Créer une copie pour ne pas modifier l'original
    arr = tableau.copy()
    n = len(arr)
    nb_comparaisons = 0
    nb_echanges = 0
    
    for i in range(n):
        # Trouver l'index du minimum dans la partie non triée
        min_idx = i
        
        for j in range(i + 1, n):
            nb_comparaisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Échanger si nécessaire
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            nb_echanges += 1
    
    fin = time.time()
    temps_execution = fin - debut
    
    return arr, nb_comparaisons, nb_echanges, temps_execution

def tri_insertion(tableau):
    """
    Tri par Insertion : Insérer chaque élément à sa place dans la partie déjà triée
    
    Args:
        tableau (list): Tableau à trier
        
    Returns:
        tuple: (tableau_trié, nb_comparaisons, nb_décalages, temps_execution)
    """
    debut = time.time()
    
    # Créer une copie pour ne pas modifier l'original
    arr = tableau.copy()
    n = len(arr)
    nb_comparaisons = 0
    nb_decalages = 0
    
    for i in range(1, n):
        cle = arr[i]
        j = i - 1
        
        # Déplacer les éléments plus grands vers la droite
        while j >= 0:
            nb_comparaisons += 1
            if arr[j] > cle:
                arr[j + 1] = arr[j]
                nb_decalages += 1
                j -= 1
            else:
                break
        
        # Insérer la clé à sa position
        arr[j + 1] = cle
        if j + 1 != i:  # Si on a effectivement déplacé l'élément
            nb_decalages += 1
    
    fin = time.time()
    temps_execution = fin - debut
    
    return arr, nb_comparaisons, nb_decalages, temps_execution

def tri_fusion(tableau):
    """
    Tri Fusion : Diviser le tableau en deux, trier récursivement, fusionner
    
    Args:
        tableau (list): Tableau à trier
        
    Returns:
        tuple: (tableau_trié, nb_comparaisons, temps_execution)
    """
    debut = time.time()
    
    # Créer une copie pour ne pas modifier l'original
    arr = tableau.copy()
    nb_comparaisons = [0]  # Liste pour pouvoir modifier dans les fonctions imbriquées
    
    def fusionner(arr, gauche, milieu, droite):
        """Fusionner deux sous-tableaux triés"""
        # Créer des tableaux temporaires
        L = arr[gauche:milieu + 1]
        R = arr[milieu + 1:droite + 1]
        
        i = j = 0
        k = gauche
        
        # Fusionner les deux tableaux
        while i < len(L) and j < len(R):
            nb_comparaisons[0] += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Copier les éléments restants
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    def tri_fusion_recursif(arr, gauche, droite):
        """Fonction récursive du tri fusion"""
        if gauche < droite:
            milieu = (gauche + droite) // 2
            
            # Trier récursivement les deux moitiés
            tri_fusion_recursif(arr, gauche, milieu)
            tri_fusion_recursif(arr, milieu + 1, droite)
            
            # Fusionner les deux moitiés triées
            fusionner(arr, gauche, milieu, droite)
    
    # Appeler la fonction récursive
    if len(arr) > 1:
        tri_fusion_recursif(arr, 0, len(arr) - 1)
    
    fin = time.time()
    temps_execution = fin - debut
    
    return arr, nb_comparaisons[0], temps_execution

def tri_rapide(tableau):
    """
    Tri Rapide : Choisir un pivot, partitionner, trier récursivement les sous-tableaux
    
    Args:
        tableau (list): Tableau à trier
        
    Returns:
        tuple: (tableau_trié, nb_comparaisons, nb_échanges, temps_execution)
    """
    debut = time.time()
    
    # Créer une copie pour ne pas modifier l'original
    arr = tableau.copy()
    nb_comparaisons = [0]  # Liste pour pouvoir modifier dans les fonctions imbriquées
    nb_echanges = [0]
    
    def partitionner(arr, bas, haut):
        """Partitionner le tableau autour du pivot"""
        # Choisir le dernier élément comme pivot
        pivot = arr[haut]
        i = bas - 1  # Index du plus petit élément
        
        for j in range(bas, haut):
            nb_comparaisons[0] += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    nb_echanges[0] += 1
        
        # Placer le pivot à sa position finale
        if i + 1 != haut:
            arr[i + 1], arr[haut] = arr[haut], arr[i + 1]
            nb_echanges[0] += 1
        
        return i + 1
    
    def tri_rapide_recursif(arr, bas, haut):
        """Fonction récursive du tri rapide"""
        if bas < haut:
            # Partitionner le tableau
            pi = partitionner(arr, bas, haut)
            
            # Trier récursivement les éléments avant et après la partition
            tri_rapide_recursif(arr, bas, pi - 1)
            tri_rapide_recursif(arr, pi + 1, haut)
    
    # Appeler la fonction récursive
    if len(arr) > 1:
        tri_rapide_recursif(arr, 0, len(arr) - 1)
    
    fin = time.time()
    temps_execution = fin - debut
    
    return arr, nb_comparaisons[0], nb_echanges[0], temps_execution

def tester_tri(fonction_tri, tableau, nom_algo):
    """
    Fonction helper pour tester un algorithme de tri
    
    Args:
        fonction_tri: Fonction de tri à tester
        tableau (list): Tableau à trier
        nom_algo (str): Nom de l'algorithme pour l'affichage
        
    Returns:
        tuple: Résultats du tri
    """
    print(f"Test de {nom_algo} sur {len(tableau)} éléments...")
    return fonction_tri(tableau)
