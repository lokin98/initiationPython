liste1 = ["a","b","c"]
#position  0   1   2 
liste2 = ["ananas", "banane", "citron"]
#position   0           1        2

# print(liste1[0])
# index = liste1.index("c")
# print("position de la lettre = ", index)

print("quelle lettre voulez vous ? a->c")
lettre =input(">>>") # on enregistre la lettre taper au clavier 

index = liste1.index(lettre) # on enregistre la lettre
print(liste2[index])