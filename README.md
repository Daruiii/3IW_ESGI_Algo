# Analyse de Performance d'Algorithmes
## Tri et Recherche sur Données Immobilières

### Objectif
Ce projet implémente **FROM SCRATCH** et compare les performances de 7 algorithmes sur des données immobilières réelles :
- **4 algorithmes de tri** : Sélection, Insertion, Fusion, Rapide
- **3 algorithmes de recherche** : Linéaire, Binaire, Min/Max

### Données
- **1000 transactions immobilières** réelles
- **8 colonnes** : date_mutation, prix, surface, commune, type_local, nb_pieces, code_postal, prix_m2
- **3 tailles de test** : 100, 500, 1000 éléments

### Utilisation
```bash
python3 main.py
```

### Structure
```
├── main.py                    # Programme principal
├── algorithmes_tri.py         # 4 algorithmes de tri
├── algorithmes_recherche.py   # 3 algorithmes de recherche
├── utilitaires.py            # Lecture CSV + mesures
├── transactions_immobilieres.csv  # Données
├── resultats.txt             # Résultats des tests
├── analyse.txt               # Analyse des 10 questions
```

### Résultats Clés
- **Tri Rapide** : Le plus efficace pour les prix (0.0038s sur 1000 éléments)
- **Tri Fusion** : Le plus stable et prévisible
- **Recherche Binaire** : 38x plus rapide que la recherche linéaire
- **Différence O(n²) vs O(n log n)** : Facteur 25-50 sur données réelles

### ⚡ Contraintes Techniques
- **Aucune bibliothèque externe** (pas de `sorted()`, `csv`, `pandas`)
- **Comptage manuel** des comparaisons et opérations
- **Mesures de temps** précises avec `time.time()`
- **Implémentation complète** de tous les algorithmes

---
**Auteur** : David - 3IW ESGI  
**Projet** : Analyse de Performance d'Algorithmes  
**Date** : 2025
