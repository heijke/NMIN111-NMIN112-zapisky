# Objektově orientované programování a třídy
## třída: atribut - proměnná, metoda - funkce, instance - objekt vytvořený ze šablonky třídy
## případné metody voláme potom tečkovou notací pomocí jména instance třídy
## vyhýbáme se tak globálním jménům proměnných a funkcí

class Osoba: # konvencí je psát jména tříd s velkým písmenem
	pass # umožní nám vynechat prostor
	def __init__(self, jm, pr, nar): # konstruktor, self značí konkrétní instanci
		self.jmeno = jm
		self.prijmeni = pr
		nar = nar.split(".")
		self.den_narozeni = nar[0]
		self.mesic_narozeni = nar[1]
		self.rok_narozeni = nar[2]
	def __repr__(self): # spouští se pokud je na třídu zavolán print
		return f"Osoba({self.jmeno}, {self.prijmeni}, {self.vek})"
	def vek(self):
		return 2025 - self.rok_narozeni # nyní neřešíme obecnou funkčnost

osoba1 = Osoba("Jan", "Novák", "1.12.2000")

## python povoluje trailing comma
## if __name__ == "__main__": spustí kód pouze pokud spouštíme přímo