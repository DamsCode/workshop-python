#Fonctions nomée
Le mot-clé def introduit une définition de fonction. Il doit être suivi du nom de la fonction et d'une liste, entre parenthèses, de ses paramètres. L'instruction qui constitue le corps de la fonction débute à la ligne suivante et doit être indentée.
```
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
```

#Fonctions anonymes
Avec le mot-clé lambda, vous pouvez créer de petites fonctions anonymes. En voici une qui renvoie la somme de ses deux arguments : lambda a, b: a+b. Les fonctions lambda peuvent être utilisées partout où un objet fonction est attendu. Elles sont syntaxiquement restreintes à une seule expression. Sémantiquement, elles ne sont que du sucre syntaxique pour une définition de fonction normale. Comme les fonctions imbriquées, les fonctions lambda peuvent référencer des variables de la portée englobante
```
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0)
f(1)
```

[Suivant](exceptions.md)