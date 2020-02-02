# for
L'instruction for que propose Python est un peu différente de celle que l'on peut trouver en C ou en Pascal. Au lieu de toujours itérer sur une suite arithmétique de nombres (comme en Pascal), ou de donner à l'utilisateur la possibilité de définir le pas d'itération et la condition de fin (comme en C), l'instruction for en Python itère sur les éléments d'une séquence (qui peut être une liste, une chaîne de caractères…), dans l'ordre dans lequel ils apparaissent dans la séquence. Par exemple :
```
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

# la fonction range
Si vous devez itérer sur une suite de nombres, la fonction native range() est faite pour cela. Elle génère des suites arithmétiques :
```
for i in range(5):
    print(i)
```

# while 
L'instruction while est utilisée pour exécuter des instructions de manière répétée tant qu'une expression est vraie :

```
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
```

#Break & else dans une boucle
L'instruction break, comme en C, interrompt la boucle for ou while la plus profonde.

Les boucles peuvent également disposer d'une instruction else ; celle-ci est exécutée lorsqu'une boucle se termine alors que tous ses éléments ont été traités (dans le cas d'un for) ou que la condition devient fausse (dans le cas d'un while), mais pas lorsque la boucle est interrompue par une instruction break. L'exemple suivant, qui effectue une recherche de nombres premiers, en est une démonstration 

```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
# continue 
L'instruction continue, également empruntée au C, fait passer la boucle à son itération suivante :

```
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
```

# pass
L'instruction pass ne fait rien. Elle peut être utilisée lorsqu'une instruction est nécessaire pour fournir une syntaxe correcte, mais qu'aucune action ne doit être effectuée. Par exemple :
```
def initlog(*args):
    pass   # Remember to implement this!
```

[Suivant](fonctions.md)