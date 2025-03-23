# Pokračování ukázek standardních knihoven - knihovna pro generování náhodných čísel

# Úvod k dnešním DÚ - permutace - budeme mít n předmětů k permutaci
## Ty budeme reprezentovat {1_n} čísly představující jednotlivé prvky
## Všechny permutace můžeme seřadit dle lexigrafického uspořádání - v pythonu standartní uspořádání
## permutace si můžeme očíslovat - čísly 1-n!
## Jaká bude struktura této množiny?
## 1 Pro nějaké dané n dostaneme zadanou permutaci nalezněte bezporstředně následující permutaci
## 2 dostaneme nějaké N, jež je mohutností množiny, nalezněte k-tou permutaci

# Formátování čísel na výstupu
## Pomocí formátovaného stringu
s = []
a = 3456
for x in s: print("f{x}")

for x in s: print("f{x:10}")
## Dpolněna nulami
for x in s: print("f{x:010}")
## S přesností na 5 desetiných míst
print("f{a:20.5f}")
## Vypsáno v exponenciálním tvaru
print("f{a:20.5e}")

# Úloha 1 - hříčka s číslama - funkce dostane jedno celé číslo a vrátí nám ciferný součet
def ciferny_soucet(cislo):
    soucet = 0
    for x in str(cislo):
        soucet += int(x)
    return soucet

## Řešení pana Topfera
def ciferny_soucet2(cislo):
    return sum(map(int, str(cislo)))
cislo = 29
print(ciferny_soucet(cislo))

# Úloha 2 - funkce dostane dvě čísla a spočítá největší společný dělitel - efektivně

# Úloha 3 - je číslo prvočislem? bool funkce