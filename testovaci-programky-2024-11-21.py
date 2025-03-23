# Pokračování v maticích

# Úkol 1 - funkce, která vygeneruje tabulku malé násobilky
def tabulka(n):
    matice = [[0]*n for _ in range(n)]
    for i in range(1,n):
        for j in range(1,n):
            matice[i][j] = i*j
    return matice

## Řešení pana Topfera
def nasobilka():
    return [[i*j] for j in range(1,11) for i in range(1,11)]

print(tabulka(10), end="\n")
print(nasobilka())

## Výpis prvků datového typu bez závorek kolem print(*n[i]) - nutno přidat hvězdičku před
## Nebo ručně
for i in range(10):
    for j in range(10):
        print(tabulka(10)[i][j], end=" ")
    print()
print()

## Nebo ještě lépe, zarovnaně
## Formátujeme řetězec, vyplníme ho vždy na čtyři místa
for i in range(10):
    for j in range(10):
        print(f"{tabulka(10)[i][j]:4}", end="")
    print()
print()

## Vyhodnocení a vypsání výrazu v print formátovaným řetězcem
z = 10
print(f"je tu {z} trpaslíků")

# Úloha 2 - transpozice matice

def transpozice(matice):
    radky = len(matice)
    sloupce = len(matice[0])
    transpovonana_m = [[0]*radky for _ in range(sloupce)]
    for i in range(radky):
        for j in range(sloupce):
            transpovonana_m[j][i] = matice[i][j]
    return transpovonana_m

## Řešení pana Topfera
def transpozice_2(matice):
    radky = len(matice)
    sloupce = len(matice[0])
    return [[ matice[j][i] for j in range(radky)] for i in range(sloupce)]

matice = [[1,2,3,4],[9,0,1,2],[5,6,7,8]]
print(transpozice(matice))

# Datové struktury množina a slovník
# Prve množiny
## V množině se hodnoty nemohou opakovat a není definováno uspořádání prvků - nejsou hojně využívané
## cokoliv jde naprogramovat pomocí množin, jde i pomocí seznamů
## pří použití množin jsou avšak prováděné operace rychlejší
## jelikož seznam je procházen popořadě,
## kdežto množina dá hash každého prvku do lookup tabulky
## k nalezení prvku nám tedy stačí pouze dvě operace (hash prvku -> je v tabulce?)
## Jejich rozdíl je tedy pouze v efektivitě
## Množina je vypisována v pořadí daném jejich umístěním v tabulce hashů

## Při opakování hodnoty se její druhý výskyt nijak nezapočítává, duplicity nemohou vzniknout,
## protože hash čísla 44 je při každém pokusu o přidání do tabulky stejný

mnozina = {44,55,66,77,88,99,22,33,44}
print(mnozina)

## Dostaneme unikátní písmena ve slově
set("ksjfg iqusghydusjiwokdjaaaaaaaaaaaa")

## Vytvoření prázdné množiny
set()

## Datový typ množiny je typu mutable - lze ho tedy přepisovat
mnozina.add(11)
mnozina.remove(44)

## Porovnání množin a == b
## Průnik množin a & b
## Sjednocení množin a | b
## Součet množin a + b
## Rozdíl množin a - b

## Možno využít jako evidence souboru dat, kde nezáleží na pořadí s efektivním přístupem k prvkům

## Dají se také vytvářet generátorovou notací
mnozina_2 = {x**2 for x in range(10)}

# Nyní slovníky (asociativní pole)
## Ukládá dvojice klíč, hodnota. Dle klíče hledáme, hodnota je na něj vázána
## klíč je hashován a uložen v tabulce - proto opět rychlé vyhledávání

## Nutné zvolit vhodný klíč, aby slovník stále zajistil rychlé vyhledávání
## Klíč musí být typu immutable

## Založení slovníku
auta = {"Skoda":14, "Opel":3, "Renault":1}

## Přidání do slovníku
auta["Fiat"] = 1

## Odstranění
del auta["Fiat"]

## Není povolené ptát se na klíč, který slovník neobsahuje - program havaruje
## auta["Fiat"]

## Musíme se zeptat jinak, pomocí metody .get()
auta.get("Fiat")

## Nebo i nastavit výchozí parametr jaký vrátit, pokud slovník klíč neobsahuje
auta.get("Fiat", -1)

## Slovník, dle generátorové notace - dvojtečkou dáme najevo, že chceme slovník a ne množinu
slovnik_kvadratu = {x:x**2 for x in range(10)}

## Iterace přes slovník
for a in auta:
    print(a) ## Vypíše klíče
    print(auta[a]) ## Vypíše hodnoty

for a in auta.keys():
    print(a) ## Také klíče

for a in auta.values():
    print(a) ## Nyní hodnoty

for a in auta.items():
    print(a) ## Nyní dostaneme dvojice klíč:hodnota jako tuple (klíč, hodnota)

# Úkol 3 - napočítat pomocí slovníku počet vyskytů jednotlivých slov

slova = ["aaa", "ahoj", "cus", "cus", "cauky", "cus", "ahoj", "cus"]

def vyskyty(seznam_slov):
    pocet_vyskytu = {}
    for slovo in seznam_slov:
        if slovo in pocet_vyskytu:
            pocet_vyskytu[slovo] += 1
        else:
            pocet_vyskytu[slovo] = 1
    return pocet_vyskytu

## Řešení pana Topfera
def vyskyty_2(seznam_slov):
    pocet_vyskytu = {}
    for slovo in seznam_slov:
        seznam_slov[slovo] = seznam_slov.get(slovo, 0) + 1

for value in vyskyty(slova).items():
    print(*value)