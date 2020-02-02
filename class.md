# Classes
Les classes sont un moyen de réunir des données et des fonctionnalités. Créer une nouvelle classe crée un nouveau type d'objet et ainsi de nouvelles instances de ce type peuvent être construites. Chaque instance peut avoir ses propres attributs, ce qui définit son état. Une instance peut aussi avoir des méthodes (définies par la classe de l'instance) pour modifier son état.
```
class Dog:

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
```

# Héritage
Ici une classe peut être hérité d'une où plusieurs classes
```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```