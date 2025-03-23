# DÚ na přístě vysvětlení:
## Součty násobky a dělení se zbytkem řídkých polynomů, kde ukládáme pouze nenulové členy
## jako posloupnost dvojic exponent koeficient

# Knihovna pro želví grafiku
## Chceme hýbat želvou po obrazovce - pomocí toho ukážeme nějaké python specifika
## 

import turtle
from math import sqrt

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.forward(100*sqrt(2))

turtle.done()

## Chceme vytovřit česou želvu
def ceska_zelva():
	dopredu = turtle.forward()
	doleva = turtle.left()
	doprava = turtle.right()
	pokracuj = turtle.done()

zelvicka = turtle.Turtle()

class TlustaZelva(turtle.Turtle):
	def __init__(self,tloustka=10):
		super().__init__()
		self.width(tloustka)
		self.pencolor("orange")

zelvak = TlustaZelva(11)
zelvak.forward(50)
zelvak.done()

# A nyní si chceme naprogramovat hru
## Myslím si zvířátko - funkční dekompozice, přepis z tabule

def generuj_slovo():
	
def tiskni_slovo():
	
def nacti_pismeno():
	
def porovnej():
	
def dopln_pismeno():
	
def tiskni_sibenici():
	
slovo = generuj_slovo()
vytiskni_slovo()

zivoty = 5
uhodnuto = False

while zivoty>0:
	pismeno = nacti_pismeno()
	if porovnej(pismeno,slovo):
		slovo = dopln_pismeno(pismeno, slovo)
	else:
		zivoty -= 1
		tiskni_sibenici()
	tiskni_slovo()
print(slovo)