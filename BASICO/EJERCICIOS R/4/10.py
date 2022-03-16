from sys import stdin


def RvD():
    lista = stdin.readline().strip()
    x = int(stdin.readline())
    k = int(stdin.readline())

    lista_1 = []

    '''El ciclo permite iterar sobre la entrada para volver los numeros de cadenas a enteros para asi evaluar el caso'''
    suma = ""
    for i in lista:
        if i == "[":
            continue
        elif i == "," or i == "]":
            suma = int(suma)
            if suma == x:
                suma = ""
                continue
            else:
                lista_1.append(suma)
                suma = ""
        else:
            suma += i

    '''El siguiente ciclo muestra los k mas cercanos a x'''
 
    lista_2 = []
    while k !=0:
        num = 0
        sum_2 = 0
        for j in lista_1:
            suma = (j-x)
            suma = abs(suma)
            if num == 0 and sum_2 == 0:
                sum_2 = j-x
                sum_2 = abs(sum_2)
                num = j
            elif sum_2 > suma:
                sum_2 = suma
                num = 0
                num = j
        
        lista_2.append(num)        
        
        lista_mod = []
        for i in lista_1:
            if i == num:
                continue
            else:
                lista_mod.append(i)
        lista_1 = lista_mod
        num = 0
        sum_2 = 0
        k-=1
    print(*lista_2)

RvD()
