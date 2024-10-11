'''
*********************************
nazwa funkcji: NWD
opis funkcji : znajduje nwd
parametry: liczba1 - liczba całkowita nr 1
                   liczba2 - liczba całkowita nr 2
zwracany typ i opis: zwraca wynik
Autor: nieznany
*********************************
'''
'''
def NWD (liczba1,liczba2):
    while(liczba1!=liczba2):
        if liczba1>liczba2:
            liczba1 -= liczba2
        else:
            liczba2 -= liczba1
    return liczba1

print(NWD (16,12))
'''




def NWDproste(a,b):
    while b>0:
        pom = a
        a = b
        b = pom % b
    return a
print(NWDproste(99,66))
