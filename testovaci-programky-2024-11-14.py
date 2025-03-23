# Pokračování řazení jmen podle příjmení
## Zavolání sorted s klíčem dle kterého porovnávat
## Kratší a přehlednější řešení
jmena = ["Jan Novak", "Eva Novakova", "Tomas Dvorak"]
def razeni_jmen(seznam_jmen):
    jm, prij = seznam_jmen.split()
    return prij, jm

print(sorted(jmena, key = razeni_jmen))

## Ještě jinak
## Odpustíme si definování jednorázové / jednoúčelové funkce
## Tedy lambda funkce - historický název z lambda kalkulu

print(sorted(jmena,
             key = lambda seznam_jmen: (seznam_jmen.split()[1], seznam_jmen.split()[0])))

# Úloha 1 - kombinace všech tří - dostaneme text - vytvořit seznam slov v textu seřazený podle délky
## (nejkratší až nejdelší)
## Slova téže délky abecedně

text = [vstup for vstup in input().split()]
print(sorted(sorted(text,
             key = lambda x: len(x))))
## Nebo ještě lépe
print(sorted(text,
             key = lambda x: (len(x),x)))

## A od nejdelšího
print(sorted(text,
             key = lambda x: (-len(x),x)))
## Nyní ale i opačně dle abecedy
print(sorted(text,
             key = lambda x: (len(x),x), reverse = True))
# Ještě jednou lambda funkce
## def f(x):
##  ........
##  return
## A nebo jako lambda
## f = lambda x: .......

## Vše je v pythonu objekt, každý objekt lze dosadit do proměnné

# Úloha 2 - seznam čísel - a chceme vytvořit seznam zbytků po dělení 7

cisla = [11, 22, 33, 44, 55]

print([num%7 for num in cisla])
## Map bere transformační funkci a seznam, který změnit
print(list(map(lambda num: num % 7, cisla)))

# Vícerozměrná pole, neboli matice
## V pythonu implementován jako seznam seznamů čísel p[i][j]
## Seznamy jsou frexibilnější, než pole
matice = [[1,2,3,4],[5,6,7,8],[9,0,1,2]]

## Načtení matice ze vstupu
m = []
pocet_radku = int(input())
for _ in range(pocet_radku):
    m.append(list(map(int, input().split())))

print(m)

## Vytvoření inicializované matice jako nulové
## Matice 3x4
m2 = [[0]*4]*3
## Ale prvky se kopírují !!!!
## Tedy změna jednoho řádku způsobí i změnu ostatních
## Stejně udělá pouze odkaz i m2.copy() // mělká kopie

## Korektní způsob
m3 = [[0]*4 for _ in range(3)]

## Hluboká kopie
## Pomocí klihovny copy
import copy
b = copy.deepcopy(m3)

# Operace na maticích
## Součet všech prvků
def soucet(matice):
    soucet = 0
    for i in range(len(matice)):
        for j in range(len(matice[0])):
            soucet += matice[i][j]
    return soucet

print(soucet(m))

print(sum(sum(radek) for radek in m))

## Součet dvou matic
def soucet(m1, m2):
    init_m = [[0]*4 for _ in range(3)]
    if len(m1) == len(m2) & len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
              init_m[i][j] = m1[i][j] + m2[i][j]

print(soucet(matice, m3))

## Součin dvou matic

def soucin(m1, m2):
    init_m = [[0] * 4 for _ in range(3)]
    n = len(m1)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                init_m[i][j] = m1[i][k] * m2[k][j]
def soucin2(m1, m2):
    init_m = [[0] * 4 for _ in range(3)]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            init_m[i][j] = sum(m1[i][k] + m2[k][j] for k in range(len(m1[0])))
print(soucin(matice, m3))

## K DÚ:
## Program na řešení soustavy n lineárních rovnic o n neznámých (+ pravá strana)
## Dostaneme regulární matici s celočíselnými koeficienty - má tedy právě jedno celočíselné řešení
## Řešit gauss-jordanovou eliminací
## Pokud by vznikla 0 na diagonále, prohodíme řádky