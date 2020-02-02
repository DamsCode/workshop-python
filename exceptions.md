# Exceptions
Même si une instruction ou une expression est syntaxiquement correcte, elle peut générer une erreur lors de son exécution. Les erreurs détectées durant l'exécution sont appelées des exceptions et ne sont pas toujours fatales : nous apprendrons bientôt comment les traiter dans vos programmes. La plupart des exceptions toutefois ne sont pas prises en charge par les programmes, ce qui génère des messages d'erreurs comme celui-ci :
```
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
La dernière ligne du message d'erreur indique ce qui s'est passé. Les exceptions peuvent être de différents types et ce type est indiqué dans le message : les types indiqués dans l'exemple sont ZeroDivisionError, NameError et TypeError. Le texte affiché comme type de l'exception est le nom de l'exception native qui a été déclenchée. Ceci est vrai pour toutes les exceptions natives mais n'est pas une obligation pour les exceptions définies par l'utilisateur (même si c'est une convention bien pratique). Les noms des exceptions standards sont des identifiants natifs (pas des mots réservés).

## Gestion exceptions
Il est possible d'écrire des programmes qui prennent en charge certaines exceptions. Regardez l'exemple suivant, qui demande une saisie à l'utilisateur jusqu'à ce qu'un entier valide ait été entré, mais permet à l'utilisateur d'interrompre le programme (en utilisant Control-C ou un autre raccourci que le système accepte) ; notez qu'une interruption générée par l'utilisateur est signalée en levant l'exception KeyboardInterrupt.
```
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

## Déclencher des exceptions
L'instruction raise permet au programmeur de déclencher une exception spécifique. Par exemple :
```
raise NameError('HiThere')
```
[Suivant](class.md)