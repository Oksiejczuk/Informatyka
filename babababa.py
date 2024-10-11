def z10naSystem(liczba,system):
    wynik=' '
    while(liczba>0):
        reszta = liczba%system
        liczba=liczba//system
        if reszta<10:
            wynik= chr(reszta+48) +wynik
        else:
            wynik= chr(reszta +55) + wynik
    return wynik

def z8naSystem(liczba):
    wynik=' '
    while(liczba>0):
        reszta = liczba%8
        liczba=liczba//8
        wynik= chr(reszta+48) +wynik
    return wynik

def zSystemNa10(tekst,system):
    wynik = 0
    for cyfra in tekst:
        if cyfra >='0' and cyfra <='9':
            wynik = wynik*system +ord(cyfra)-48
        else:
            wynik = wynik*system + ord(cyfra)-55
    return wynik

def z4lub8Na10(tekst,system):
    wynik = 0
    for cyfra in tekst:
            wynik = wynik*system +ord(cyfra)-48
    return wynik

#print(z10naSystem(30,2))
#print(z8naSystem(30))
#print(zSystemNa10('1E',16))
print(z4lub8Na10('53',8))
