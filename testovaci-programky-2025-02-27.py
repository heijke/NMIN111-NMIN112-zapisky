# Opakování z minulého semestru
## Řezy vytvářejí kopii seznamu
## Generátorová notace cisla = [int(c) for c in input() if len(c)>3]
## Platnost proměnných definovaných ve funkci je pouze v rámci funkce
## Formátovaný výstup print("vysledek je", v, "Kč", sep="") a nebo print("vysledek je" + v + "Kč") a nebo print(f"vysledek je {v:.2f}Kč")
## Po proměnné v {} může následovat formátovací řetězec za : -> {promenna:.2f}
## Poznámka - u zápočtového testu je povolena docs.python.org
## Práce se soubory, prve potřebujeme nějaký textový soubor
f = open("pokus.txt", encoding="utf-8")
obsah = f.read(5) # například kolik chceme přečíst znaků
f.readline() # jedna řádka
radky = f.readlines() # všechny řádky a uloží je do seznamu řádek

for r in radky:
	print(r.rstrip())

for radek in f:
	print(radek)


f.close()
print(obsah)

with open("pokus.txt", encoding="utf-8") as file:
	for radek in file:
		print(radek)

f = open("pokus-1.txt", "w", encoding="utf-8")
f.write("bbbbbbbbbbbbbbbSDEščř")

## Standardní knihovny (v pythonu pojmenovány moduly) jsou součástí instalace pythonu
## lze je nalézt v dokumentaci
## Přehled zabudovaných modulů můžeme zístat jako puštění offline dokumentace
## Knihovna copy - 
import copy 
s = [1, 0, 50, 5514352, 21]
s1 = copy.copy(s) # Pokud bychom provedli s1 = s, pak s1 pouze ukazuje na s a jakákoliv změna v s1 ovlivní i s a naopak
s2 = copy.deepcopy(s) # Pokud by s obsahovalo i další vnořené seznamy vykopíruje i ty

## Knihovna array -
## Pro práci s polem můžeme v ythonu využít i seznam (v jiných jazycích musejí být v poli všechny hodnoty stejného typu)
## Knihovna fractions -
## Umožňuje nám počítat se zlomky
## Knihovna decimal - 
## Umožňuje nám reprezentovat přesně desetinná čísla
## Knihovna time -
## Možnost přesnějšího měření času
## Knihovna random -
## Generování náhodných čísel

## Výjimky a chyby - 
## Výpis chyby interpreterem - vidíme na kterém řádku a třídu chyby
## Můžeme s nimi i pracovat anižby nám padal program
## assert - způsob ladění programu (namísto nehezkých print statements!!)

##  Třídy a objekty -

## Poznámka DÚ - tento je zahřívací, udělejte kód krásným <3
## Tím, co to znamená se budeme zabývat později.

## Poznámka - používat rozumné vývojové prostředí