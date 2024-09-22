# Utilisation de sorted avec key
liste = [(1, 2), (3, 1), (5, 4)]
# Trier par le deuxième élément de chaque tuple
sorted_list = sorted(liste, key=lambda x: x[1])
print("Trier par le deuxième élément de chaque tuple\n")
print(sorted_list)


# Trier une liste de strings par la longueur de chaque string
strings = ["aaaa", "bb", "c"]
sorted_strings = sorted(strings)  # Trier par ordre alphabétique
sorted_strings_len = sorted(strings, key=len)  # Trier par la longueur de chaque string
print("Trier une liste de strings\n")
print(sorted_strings)
print("Trier par la longueur de chaque string\n")
print(sorted_strings_len)