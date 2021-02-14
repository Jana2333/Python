#!/usr/bin/env python3

# Tento kód spadá pod licenci ITnetwork Premium -
# http://www.itnetwork.cz/licence
# Je určen pouze pro osobní užití a nesmí být šířen
# ani využíván v open-source projektech.

import os

# kód na vymazání obrazovky konzole
clear = lambda: os.system(['clear','cls'][os.name == 'nt'])

hrac = 2
konec = False
znaky = [" ", "O", "X"]
hraci = ["nikdo", "hráč s kolečky", "hráč s křížky"]
plocha = []
RADKU = 9
SLOUPCU = 9
for i in range(RADKU):
    radek = []
    for j in range(SLOUPCU):
        radek.append(0)
    plocha.append(radek)

while not konec:
    clear() # vymazání konzole
    # první řádek s čísly
    print(" ", end="")
    # vykreslení pl
    for k in range(1, RADKU+1):
        print(k, end="")
    print("")
    # vykreslení hrací plochy
    for x, radek in enumerate(plocha):
        print(x+1, end="")
        for y, policko in enumerate(radek):
            print(znaky[policko], end="")
        print("")
    # kontrola výhry
    symbolu_vyhra = 5
    zaplneno = 0
    symbolu_radek = 0
    symbolu_sloupec = 0
    for x in range(RADKU):
        for y in range(SLOUPCU):
            if plocha[x][y] > 0:
                zaplneno += 1
            if zaplneno == RADKU*SLOUPCU:
                print("Remíza")
                konec = True
            # Počítání souvislých symbolů posledního hráče na tahu v řádku
            if plocha[x][y] == hrac:
                symbolu_radek += 1
            else: # Symbol nebyl nalezen, vynulujeme počítadlo nepřerušené řady symbolů
                symbolu_radek = 0

            # Počítání souvislých symbolů posledního hráče na tahu ve sloupci
            if plocha[y][x] == hrac:
                symbolu_sloupec += 1
            else: # Symbol nebyl nalezen, vynulujeme počítadlo nepřerušeného sloupce symbolů
                symbolu_sloupec = 0
            # Vyhodnocení výhry řadou nebo sloupcem
            if symbolu_radek == symbolu_vyhra or symbolu_sloupec == symbolu_vyhra:
                print("Vyhrál", hraci[hrac])
                konec = True
            
    # Diagonály - tady je to horší :)
    symbolu_diagonala_leva = 0 # Počet stejných symbolů za sebou v diagonále zleva doprava
    symbolu_diagonala_prava = 0 # Počet stejných symbolů za sebou v diagonále zprava doleva

    # 2 vnořené cykly postupně projedou všechny diagonály

    # Projíždíme 2x více řad než má hrací plocha, jinak bychom nalezli jen polovinu diagonál
    for j in range(SLOUPCU*2):
        for i in range(RADKU):
            # Diagonála zprava doleva
            dy = SLOUPCU - 1 - j + i # Postupujeme od posledního řádku nahoru
            if 0 <= dy < SLOUPCU and (plocha[RADKU - 1 - i][dy] == hrac): # Nevyjeli jsme z plochy a našli jsme hráčův kámen
                symbolu_diagonala_leva += 1
            else:
                symbolu_diagonala_leva = 0 # Jsme mimo nebo tam hráč nemá kámen

            # Diagonála zleva doprava
            if 0 <= dy < SLOUPCU and (plocha[i][dy] == hrac): # Nevyjeli jsme z plochy a našli jsme hráčův kámen
                symbolu_diagonala_prava += 1
            else:
                symbolu_diagonala_prava = 0 # Jsme mimo nebo tam hráč nemá kámen
            # Vyhodnocení výhry jednou z diagonál
            if symbolu_diagonala_leva == symbolu_vyhra or symbolu_diagonala_prava == symbolu_vyhra:
                print("Vyhrál", hraci[hrac])
                konec = True

    if not konec:
        # Prohození hráčů
        if hrac == 1:
            hrac = 2
        else:
            hrac = 1
        print("\nNa řadě je", hraci[hrac])
        volno = False
        x = 1
        y = 1
        # Načítání souřadnic dokud nezadá takové, kde je volno
        while not volno:
            zadano = False
            while not zadano:
                try:
                    x = int(input("Zadej pozici X kam chceš tahnout: "))
                    zadano = True
                except ValueError:
                    print("Zadej prosím celé číslo")
            zadano = False
            while not zadano:
                try:
                    y = int(input("Zadej pozici Y kam chceš tahnout: "))
                    zadano = True
                except ValueError:
                    print("Zadej prosím celé číslo")
            if 1 <= x <= 9 and 1 <= y <= 9 and plocha[y - 1][x - 1] == 0:  # Souřadnice jsou v hrací ploše a není tam hráčův kámen
                volno = True
            else:
                print("Neplatná pozice, zadej ji prosím znovu.")
        plocha[y - 1][x - 1] = hrac # Uložení kamene hráče do hrací plochy

input()
