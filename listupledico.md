# List

Python connaît différents types de données combinés, utilisés pour regrouper plusieurs valeurs. Le plus souple est la liste, qui peut être écrit comme une suite, placée entre crochets, de valeurs (éléments) séparées par des virgules. Les éléments d'une liste ne sont pas obligatoirement tous du même type, bien qu'à l'usage ce soit souvent le cas.

```
squares = [1, 4, 9, 16, 25]
print(squares)
```

#tuple


```
t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
```

Comme vous pouvez le voir, les tuples sont toujours affichés entre parenthèses, de façon à ce que des tuples imbriqués soient interprétés correctement ; ils peuvent être saisis avec ou sans parenthèses, même si celles-ci sont souvent nécessaires (notamment lorsqu'un tuple fait partie d'une expression plus longue). Il n'est pas possible d'affecter de valeur à un élément d'un tuple ; par contre, il est possible de créer des tuples contenant des objets muables, comme des listes.

Si les tuples peuvent sembler similaires aux listes, ils sont souvent utilisés dans des cas différents et pour des raisons différentes. Les tuples sont immuables et contiennent souvent des séquences hétérogènes d'éléments qui sont accédés par "déballage" (voir plus loin) ou indexation (ou même par attributs dans le cas des namedtuples). Les listes sont souvent muable et contiennent des éléments homogènes qui sont accédés par itération sur la liste.


#dictionnaire

Un autre type de donnée très utile, natif dans Python, est le dictionnaire (voir Les types de correspondances — dict). Ces dictionnaires sont parfois présents dans d'autres langages sous le nom de "mémoires associatives" ou de "tableaux associatifs". À la différence des séquences, qui sont indexées par des nombres, les dictionnaires sont indexés par des clés, qui peuvent être de n'importe quel type immuable ; les chaînes de caractères et les nombres peuvent toujours être des clés. Des tuples peuvent être utilisés comme clés s'ils ne contiennent que des chaînes, des nombres ou des tuples ; si un tuple contient un objet muable, de façon directe ou indirecte, il ne peut pas être utilisé comme une clé. Vous ne pouvez pas utiliser des listes comme clés, car les listes peuvent être modifiées en place en utilisant des affectations par position, par tranches ou via des méthodes comme append() ou extend().

Le plus simple est de considérer les dictionnaires comme des ensembles de paires clé: valeur, les clés devant être uniques (au sein d'un dictionnaire). Une paire d'accolades crée un dictionnaire vide : {}. Placer une liste de paires clé:valeur séparées par des virgules à l'intérieur des accolades ajoute les valeurs correspondantes au dictionnaire ; c'est également de cette façon que les dictionnaires sont affichés.
```
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel
```

[Suivant](conditions)