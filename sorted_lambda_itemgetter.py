from operator import itemgetter

# Liste de tuples (nom, âge, taille en cm)
personnes = [
    ("Alice", 25, 165),
    ("Bob", 30, 180),
    ("Charlie", 22, 175),
    ("David", 35, 170),
    ("Eve", 28, 160)
]

# Tri par âge en utilisant lambda
tri_age_lambda = sorted(personnes, key=lambda x: x[1])

# Tri par âge en utilisant itemgetter
tri_age_itemgetter = sorted(personnes, key=itemgetter(1))

# Tri par taille en utilisant lambda
tri_taille_lambda = sorted(personnes, key=lambda x: x[2], reverse=True)

# Tri par taille en utilisant itemgetter
tri_taille_itemgetter = sorted(personnes, key=itemgetter(2), reverse=True)

# Affichage des résultats
print("Tri par âge avec lambda:")
for personne in tri_age_lambda:
    print(personne)

print("\nTri par âge avec itemgetter:")
for personne in tri_age_itemgetter:
    print(personne)

print("\nTri par taille (décroissant) avec lambda:")
for personne in tri_taille_lambda:
    print(personne)

print("\nTri par taille (décroissant) avec itemgetter:")
for personne in tri_taille_itemgetter:
    print(personne)