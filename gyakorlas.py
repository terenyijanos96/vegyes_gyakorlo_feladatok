import random

sorozat = [-3, 5, 11, -2, 4]

def separator(sep=" "):
    s = ""
    i = 0
    while i < len(sorozat):
        s += str(sorozat[i])

        if i < (len(sorozat) - 1):
           s += f"{sep} "
        i+=1
    print(s)

def random_szam_hozzado_az_elso_szamhoz():
    rand = int(random.random() * 8) + 5
    sorozat[0] += rand

def utolso_szamjegy_helyett_ketjegyu_harommal_oszthato():
    szam = int(input("Kérek egy kétjegyű, hárommal osztható számot! (pl: 33): "))
    while not (9 < szam < 100 and szam % 3 == 0):
        szam = int(input("Nem jó! Egy kétjegyű, hárommal osztható számot kérek!: "))

    sorozat[len(sorozat)-1] = szam

def elso_ketjegyu():
    i = 0
    while not(9 < sorozat[i] < 100):
        i+=1

    print(f"Első kétjegyű szám indexe: {i}, értéke: {sorozat[i]}")

def prime(szam):
    i = 2
    while i < szam**(0.5):
        if szam % i == 0:
            return True
        i+=1

    return False

def hany_prime():
    i = 0
    c = 0
    while i < len(sorozat):
        if prime(sorozat[i]):
            c+=1
        i+=1

    print("ennyi prímszám van a sorozatban:", c)
