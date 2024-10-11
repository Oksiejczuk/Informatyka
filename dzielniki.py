
        
def ileDzielnikow(liczba):
    ile = 0
    for i in range(1, int(liczba**0.5 )+ 1):
        if liczba % i == 0:
            ile += i + n//i
            if i*i == liczba:
                ile -=i

    return ile
print(ileDzielnikow(100))


defPierwsza(liczba):
    ile = 0
    for i in range(1, int(liczba**0.5 )+ 1):
        if liczba % i == 0:
            ile += i + n//i
            if i*i == liczba:
                ile -=i

    return ile==2;
print(ileDzielnikow(100))


def czyPierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2, int(liczba**0.5) +1):
        if liczba %i == 0:
            return False
        else:
            return True

print(czyPierwsza(10))
