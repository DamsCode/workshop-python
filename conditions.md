# if
Pas besoin d'une grande définition pour expliquer les conditions cette exemple devrait suffir:

```
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

[Suivant](boucles.md)