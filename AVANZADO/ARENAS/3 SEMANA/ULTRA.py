from sys import stdin
def mergesort2(ciro, longi, mid, lado, lado2, i, j):
    cont = 0
    for x in range(ciro, longi):
        if i == (mid-ciro):
            lista[x] = lado2[j]
            j += 1
        elif j == longi-mid:
            lista[x] = lado[i]
            i += 1
        else:
            if lado[i] <= lado2[j]:
                lista[x] = lado[i]
                i += 1
            else:
                lista[x] = lado2[j]
                j += 1
                cont += (mid-ciro)-i
    return cont

def mergesort(mid, ciro, longi):
    global lista
    i = 0
    j = 0
    lado = lista[ciro:mid]
    lado2 = lista[mid:longi]
    return(mergesort2(ciro, longi, mid, lado, lado2, i, j))

def segunda(ciro, longi):
    global lista
    cont = 0
    if (ciro+1)<longi:
        mid = ((longi-ciro)//2)+ciro
        cont = segunda(ciro, mid)
        cont += segunda(mid, longi)
        cont += mergesort(mid, ciro, longi)
    return cont

def YoLo():
    global lista
    x = int(stdin.readline().strip())
    while x != 0:
        lista = []
        for i in range(x): num2 = stdin.readline().strip();lista.append(int(num2))
        cont = 0
        a = segunda(0, len(lista))
        print(a)
        x = int(stdin.readline().strip())
YoLo()

