# Úprava vstupu, separace hodnot
## Metoda input() načítá jako typ string
## Pomocí metody split() rozdělíme řetězec na jednotlivá čísla podle separátoru

# Načtení vstupu poprvé
## a = input()
## b = a.split()
## s = [];
## for c in b:
##  s.append(int(c))

## Nebo výše lépe
## s = []
## for c in input.split():
##  s.append(int(c))

## Nebo výše ještě lépe pomocí generátorové notace
## Samotný seznam se sám naplní
## s = [int(x) for x in input().split()]
## vnitřek hranatých závorek je generátor (funkce),
## která po pořadě vrací hodnoty

## Nebo výše ještě jinak
## s = map(int, input().split())
## map() je mapovací funkce. Prvním parametrem je nějaká funkce, dalším nějaký seznam
## tj. zde "převeď na int všechny načtené znaky"
## map() je také generátor
## map(sin, hodnoty) - načtený všech hodnot sinu pro hodnoty ze seznamu
## map() tedy obecně provádí něco se seznamy

# Úloha 1 - posloupnost čísel, kolik je v ní unikátních hodnot

## Mé řešení
def uniq(hodnoty):
    uniq = []
    for i in hodnoty:
        if hodnoty.count(i) == 1:
            uniq.append(i)
    return len(uniq)

seznam_hodnot = [int(x) for x in input().split()]
print(uniq(seznam_hodnot))

## Řešení pana Topfera
## Seznam s je procházen, ale není modifikován
def pocet1(s):
    h = []
    for x in s:
        if x not in h:
            h.append(x)
    return len(h)

## Seznam s je procházen a modifikován - postupně odebírány hodnoty
## Po skončení volání pocet2() bude seznam prázdný
## Vedlejším efektem je tedy smazání seznamu - nutno třeba s.copy()
## s totiž ukazuje přímo na strukturu původního seznamu
def pocet2(s):
    p = 0
    while s:
        p += 1
        x = s[0]
        while x in s:
            s.remove(x)
    return p

## Seznam s je procházen a modifikován
## Po skončení volání pocet3() bude seznam seřazený
def pocet3(s):
    s.sort()
    p = 1
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            p += 1
    return p

s = [int(x) for x in input().split()]
print(pocet1(s))
#print(pocet2(s))
#print(pocet3(s))

# Úloha 2 - výpis výsledků na jeden řádek se separátorem
## print(x, end=" ") - neodřádkuje, zakončí mezerou namísto "\n"
## print(a,b,c) - vypíše na jeden řádek oddělené čárkami
## print(a,b,c, sep="\n") - výpíše oddělené separátorem

# Úloha 3 - výpis posloupnosti seřazené podle velikosti

## Stejný princip, jako v DÚ -
## Načteme také vstupní seznam
## Zavoláme naši funkci slévání, ale první zadaný seznam bude prázdný
## z = slij([],y)

## Řešení pana Mareše - select sort, který řadí na místě (kvadratická složitost)
x = [31, 41, 59, 26, 53, 58, 97]

def select_sort(x):
    n = len(x)
    for i in range(i+1, n):
        pmin = i
        for j in range(i+1,n):
            if x[j] < x[pmin]:
                pmin = j
        x[i], x[pmin] = x[pmin], x[i]
    return x

# Řezy v seznamu (mňam)
## nějaký seznam s = [.......]
## s[2] - hodnota na pozici 2
## s[2:7] - hodnoty z pozic 2 až 6 (2:(7-1) jsou indexy prvků, které se vyříznou). Tedy řez od indexu 2 do indexu 7 vyjma
## s[2:] - hodnoty z pozic 2 až do konce seznamu
## del s[2:7] - odstranění vybraných hodnot seznamu
## s[2:7] = [15,16,17]
## s[3:3] = [15,16,17] - zařadí za třetí prvek
## s[2:7:2] - skok o dva v řezu (každý druhý prvek)
## s[2:7:-1] - jde pozpátku
## s[::-1] - celý seznam pozpátku !!! naprosto jednoduše

# Generátorová notace seznamu
## s = [co máme dát do seznamu?; pro jaké hodnoty? jak je získáme?]
## s = [x^2 for x in range(10,20)] - kvadráty čísel od 10 do 19
## s = [x^2 for x in range(10,20) if x % 2 == 1] - kvadráty lichých čísel od 10 do 19
## s = [x+y for x in range(10) for y in [3,5,7]] - součet dvojic kartézského součinu
## s = [(x,y) for x in range(10) for y in [3,5,7]] - kartézský součin (dvojice typu tuple)
## Generátor můžeme konverzními funkcemi změnit na žádoucí typ (seznam, tuple, set)
## nebo třeba jako proměnnou funkce - sum(generator)

# Datový typ tuple
## Jak se liší n-tice od seznamu?
## Všechny datové typy v pythonu jsou dvou kategoríí - mutable, immutable
## n-tice jsou immutable (po přiřazení nelze měnit), kdežto seznamy jsou mutable (lze libovolně upravovat)
## Operace s nimi jsou místy rychlejší, než se seznamy
## Hodí se například pokud chceme mít funkci, která vrací více hodnot (v jedné struktuře). Vrací tedy n-tici hodnot
