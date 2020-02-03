import random
listNom = ["BatEau","maison","bus"]
mot = random.choice(listNom).lower()
tabLettre = []
nbrVie = 8

for num in range(0, len(mot)):
    tabLettre.append(mot[num])
tabrep = ["*"]*len(mot)
tabE = []


while nbrVie > 0 and tabrep.count("*") != 0:
    print(tabLettre)
    print(tabrep)
    lettre = input("Entrez une lettre :").lower()
    if not lettre.isalpha() or len(lettre) != 1:
        print("erreur tu dois entrer une seul lettre")
        continue
    if lettre not in tabE:
        tabE.append(lettre.lower())
    else:
        print("tu as deja tester cette lettre là")
        continue

    if lettre in tabLettre:
        while tabLettre.count(lettre) != 0:
            index = tabLettre.index(lettre)
            tabrep[index] = lettre
            del tabLettre[index]
            tabLettre.insert(index, "*")
    else:
        nbrVie -= 1
        print("mauvaise reponse")
        print("il vous reste {} vies".format(nbrVie))
        continue

if tabLettre.count("*") == len(tabrep):
    print("félicitation vous avez trouvé le mot {}".format(mot.upper()))
else:
    print("Dommage vous avez perdu le mot était {}".format(mot.upper()))


# print(lettre)
