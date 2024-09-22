# sort() : modifie la liste d'origine ==> méthode

fruits = ["banane", "pomme", "cerise", "date"]
fruits.sort()
print("fruits.sort() :\n")
print(fruits)

print("_" * 50)

# sorted() : ne modifie pas la liste d'origine ==> fonction

nombres = [3, 1, 4, 1, 5, 9, 2]
nouveau_nombres = sorted(nombres)
print("Original :", nombres)
print("Trié :", nouveau_nombres)

"""
sort() est une méthode de liste.
sorted() peut etre utilisé avec n'importe quel iterable, c'est une fonction.
"""

# Itérables : listes, tuples, dictionnaires, ensembles(set), chaînes de caractères, fichiers, range, generator