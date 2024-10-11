def rozklad(n):
    L = []
    d = 2
    while d*d <= n :
        if n%d == 0:
            L.append(d)
            n = n//d
        else:
            d +=1
    if n > 1 :
        L.append(n)
    return L
k= int(input())
LL=[]
for i in range(k):
    n=int(input())
    LL = rozklad(n)
    print(*LL, sep = "*")


