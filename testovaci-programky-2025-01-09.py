# Práce s chybami - chráněné sekce
## Z kódu, který by mohl způsobit chybu uděláme chráněnou sekci - tedy zahrneme ho do try: bloku
## a pokud nastane chyba, tak nám dává možnost ji ošetřit pomocí except: bloku. Program normálně pokračuje.
## Můžeme poskytnout i více except: bloků, kde každý se soustředí pouze na určité chyby
## a podle typu chyby se vykoná akce. Na konec pak následuje except: blok bez parametrů, který zachytí všechny ostatní chyby.
## Případně můžeme mít ještě blok else: a ten nastane pokud nenastala v try: bloku žádná chyba.
## Případně ještě můžeme mít blok finally: který proběhne vždy po ukončení try: bloku - obvykle uvolňuje zdroje.

## try: bloky mohou být zanořeny i do sebe a chyby mohou propadat do vyšších try: bloků a ty se snaží ošetřit.
## Pokud je neošetří ani ty, propadá se chyba až do místa volání funkce. Pokud žádná z vyšších úrovní nechce chybu ošetřit
## - až pak způsobí běhovou chybu.

## výjimky jsou také objekty

## Přerušení programu - Ctrl+C vyvolává výjimku KeyboardInterrupt

## raise RuntimeError("...") - umožní sám vyvolat výjímku - pro potřeby ladění
## assert <podmínka> - pokud je podmínka splněna nic se neděje - pokud není - vyvstane běhová chyba AssertimeError.
## - slouží pro ladění

# Úvod objektového programování
## v pythonu je vše objektem
## V objektovém programování rozeznáváme třídy a objekty
## Třídy jsou typy objektů - předdefinované v knihovnách, nebo si můžeme vyrobit vlastní
    ## Třída obsahuje data - ruzné vlastnosti/parametry
    ## a obsahuje metody (funkce ve třídě) - kterými s objektem pak můžeme manipulovat
## Instancemi třídy jsou konkrétní objekty
## S instancemi pracujeme pomocí tečkové notace
## Při psaní velkého programu nám objektový návrh pomůže v přehlednosti a srozumitelnosti kódu - také v návrhu
## Objekty jsou nástroj pro dekompozici kódu a jeho zkvalitnění

## Dekompozice na nižší úrovní znamená rozdělení do funkcí
## Na vyšší úrovni znamená rozdělení souvisejících funkcí a jim relevantních dat do objektů
## Relevantní data mohou být veřejná či privátní - a můžeme to o nich říct
## V pythonu jsou všechny veřejné - ale přístup k některým je uživateli silně znepříjemněn, ty začínají _ či __
## Můžeme odvozovat třídy z jiných a konkrétním objektům MŮŽEME POSLÉZE PŘIDÁVAT ATRIBUTY :O

# Příklad 1 - chceme formátovat posloupnost slov na určitou šířku řádky, pro dlouhý vstup! TEDY NEVEJDE SE NÁM DO PAMĚTI
## Řešení objektovou dekompozicí - třídy Čtečka a Zapisovačka

## Magické metody - jméno ve formátu __metoda__

# Iterační metody
## Tedy k cílové hodnotě se postupně přibližuji abych se jí přiblížil s chybou nejvýše epsilon..

# Úloha 1 - z čísla n chceme spočítat jeho druhou odmocninu - buď podle vzorce, nebo podle

def skoro_odmocnina(n):
    chyba = 1/1000
    odmocina, predchozi = n, 0
    iteraci = 0
    while (abs(odmocina-predchozi)>chyba):
        predchozi = odmocina
        odmocina = (1/2)*(odmocina+(n/odmocina))
        iteraci += 1
    return odmocina, iteraci

cislo = int(input())
print(skoro_odmocnina(cislo))

def puleni_odmocnina(n):
    chyba = 1/10
    if n>1:
        spodni, horni = 1, n
    elif 0<n<1:
        spodni, horni = 0,1
    while abs(spodni-horni)>chyba:
        stred = (abs(spodni-horni))/ 2
        if n < stred ** 2:
            horni = stred
        else:
            spodni = stred
        stred = (abs(spodni - horni)) / 2
    return stred

print(puleni_odmocnina(cislo))