# Seznamy, n-tice, funkce
## Zipování seznamů - máme dva seznamy a chceme je spojit dohromady
## seznam = zip(s1, s2) - vyrobí senzam dvojic
## Pokud je jeden seznam kratší než druhý - spojí se do délky kratšího
## Nebo zip pomocí generátoru - seznam = [(p[i], v[i]) for i in range(min(len(p), len(v))]
##

# Úkol 1 - skalární součin vektorů
u = (3, 5, 15)
v = (4, 11, -6)
skalar = sum(i*j for i,j in zip(u, v))

# Znakové řetězce (string)

## Reprezentovaný jako řetězec znaků, immutable
## Možné je spojovat str + "další znaky"
## Možno dělat řezy str[:4]
## Můžeme skrze něj iterovat
## Metody: .upper() , .lower() , .capitalize() , .find(co, odkud, kam) , \
## .replace() [nahrazuje všechny podřetězce] , .split() , .strip() [obere řetězec o bílé znaky] , \
## "čím spojit".join(co spojit)

## Existuje v nich uspořádání (lexiograficky)
## "abc" < "ade"; "ab" < "abc"
## Porovnávání stringů indukuje metodu sort
## Uspořádání definováno ascii tabulkou - řazení funguje spolehlivě pouze pro anglické řetězce

## Typová konverze
## list("abc") - dostanu seznam znaků (pole charů <3)
## str(["a", "b", "c"]) - převede seznam znaků na seznam znaků ve stringu tj doslovně "["a", "b", "c"]"
## Kdežto "".join("["a", "b", "c"]) dá žádoucí "abc"

# Úloha 2 - program, který dostane na vstupu číslo n (kladné celé) a vypíše n řádků s hvězdičkami v pyramidě

n = int(input())

for i in range(n):
    print((n-i-1)*" " + (2*i+1)*"*",)

# Úloha 3 - seznam jmen seřazen abecedně podle příjmení (pokud stejné příjmení tak podle křestního jména)

jmena = ["Jan Novak", "Eva Novakova", "Tomas Dvorak"]

def razeni(seznam):
    jmeno, prijmeni = []
    for i in range(seznam):
        jmeno[i], prijmeni[i] = seznam[i].split()
    zip(jmeno, prijmeni)

## Řešení pana Topfera
def razeni2(seznam):
    t = [x.split() for x in seznam]
    u = sorted((x[1], x[0]) for x in t)
    return [jm + " " + pr for pr , jm in u]

print(razeni2(jmena))