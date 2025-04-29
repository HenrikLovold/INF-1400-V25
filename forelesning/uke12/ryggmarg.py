# Forkunnskaper
## Variabler
## Matematiske operasjoner
## Boolske uttrykk
## Løkker
## Valg
## Funksjoner

import math

a = 5
b = a + 2
c = math.sqrt(a)
for _ in range(5):
    d = a + b
print(d)

while(d < 100):
    print(d)
    d += 40

if d > 50 and b < 30:
    print("Vi er i midten")


def minfunksjon(a, b):
    return a + b

print(minfunksjon(c, d))

# Grunnleggende konsepter
## Objekter
## Metoder
## Klasser
## Arv
## is-a vs. has-a
## Polymorfi
## Grensesnitt
## Innkapsling

def f(elementer):
    return len(elementer)
f("Hello")

class Bil:
    def __init__(self, vekt):
        pass

class Garasje:
    def __init__(self, størrelse):
        self.bil = None
class A:
    def print(s):
        print("Hallo fra A")
class B:
    def print(s):
        print("Hallo fra B")
class C(B, A):
    pass

def print_klasse(instans):
    print(f"Hallo fra {type(instans).__name__}")

c = C()
c.print()
B.print(c)
print_klasse(c)


class E:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

# Verktøy
## Profilering
## Debugging
### gdb/lldb, pdb, print (?)
## Versjonskontroll
### git
## Klassediagram

# Ferdigheter som bygger videre
## Design
### Klasser som ikke trenger å være klasser
### Mange linjer i en fil
### Mange filer
### Flere klasser i samme fil - med mindre de er små og tett knyttet sammen
### Nesta if-statements
#### P Happy path bør være klar
#### P If statements for å avvike fra happy path
#### P Happy path i else
### P Fornuftige variabelnavn
#### Beskrive godt nok - men ikke for lange
### P Funksjons- og variabelnavn i stedet for kommentarer
### Hvis koden ikke kan leses og forstås så er den ikke bra
### P pep8-kode
### Mange operasjoner på en linje kode
### Tabs i stedet for spaces
### Hvis en funksjon bare blir brukt en plass - smell
### Refleksjon
## Feilsøking

