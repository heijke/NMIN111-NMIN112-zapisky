# counter(str) - vytvoří malý slovníček znaků nějakého typu
# Soubory
## Komunikace programu a souboru - pro velké vstupy a výstupy
## Jak program pracuje se soubory? Máme soubory dvou typů - textové a binární
## Textový soubor je posloupností jednotlivých znaků, členěn na řádky
## Musí se zpracovávat zásadně sekvenčně - vše popořadě.
## V jednom okamžiku do souboru můžeme pouze zapisovat nebo pouze číst - nikoliv obojí.
## Binární soubor - data jsou uložena binárně tak, jak s nimi následně pracuje počítač, slouží ke zpracování dat programy
## Umožňují indexování záznamů a jejich změny hodnot
## Transformaci do binární podoby nazýváme serializaci

## Životní cyklus souboru při práci s ním v programu má tři kroky - 1. otevření, 2. operace, 3. zavření
## Všechny operace čtení i zápisu jsou buffered - k otevřenému souboru je připojen také buffer,
## do kterého se ukládají naše operace.
## Součástí zavření programu je přenesení i neúplně naplněného bufferu.
## Pokud soubor nezavřeme korektně, změny se neprovedou a zůstávají v bufferu -
## který je po konci programu zahozen.

## Otevření souboru - open(soubor, mód přístupu), kde módy přístupu jsou: r -čtení, w - zápis, a - append (připisovat)
## Rozdíl mezi w, a - při w se vytvoří nový soubor, při a se pouze přidává nakonec
## Případně dáváme třetí argument - informaci o kódování souboru
## open() jako návratovou hodnotu vrací file handler, kterým k souboru můžeme přistoupit.
## Vše další budeme provádět voláním metod tohoto file handleru

## Čtení ze souboru - fh.read() - vrátí celý obsah textového souboru
## fh.read(n) - načte pouze n znaků, příliš nevyužíváno
## fh.readline() - přečte ze souboru jeden řádek, prochází soubor po řádcích a umožňuje ho také zpracovávat po řádcích
## pozor - řádky jsou čteny i s ukončovacími sekvencemi
## Jak poznám, že jsem na konci souboru? Volání funkce readline vrátí prázdný řetězec
## filehandler je iterovatelný cyklem - při každém čtení dostáváme další řádek - for line in file:

## Zápis do souboru - využívám metodu fh.write('co chci zapsat') - bere POUZE jeden argument typu string - bere formátované stringy
## Nebo pomocí print(co, 'neco dalsiho', file=fh)

## Uzavření souboru - fh.close()

## Vše až na open jsou metody filehandleru - jen open ne, protože to teprve vytváří filehandler.

# Úloha 1 - soubor a.txt kladných celých čísel různě v řádcích
def maximum(soubor):
    soubor = open(soubor, 'r')
    maximum = -1
    for radek in soubor:
        cisla = radek.split()
        if int(max(cisla)) > maximum:
            maximum = int(max(cisla))
    soubor.close()
    return maximum

## Řešení pana Topfera

def maximum2(soubor):
    soubor = open(soubor, 'r')
    maximum = -1
    for radek in soubor:
        v = max(v,max(map(int, radek.split())))
    soubor.close()
    return maximum
print(maximum('a.txt'))

## Další varianta jak pracovat se soubory - otevírání / závírání
## Konstrukce with - použítí kontextu
## with open('a.txt','r') as inp, open('b.txt','w') as out:
##  s = inp.read()
##  out.write(s)
## Abstrahuje otevření / zavření souboru, nemusíme se starat o jejich zavírání a případné chyby

# Úloha 2 - v souboru a.txt jsou uloženy texty / čísla, chceme ze všech znaků jedna udělat znak dva.
with open('a.txt', 'r') as inp, open('b.txt', 'w') as out:
    for radek in inp:
        out.write(radek.replace('1', '2'))

# Úloha 3 - zkopírovat max 10 řádků do dalšího souboru
with open('a.txt', 'r') as inp, open('b.txt', 'w') as out:
    for _ in range(10):
        out.write(inp.readline())