from sys import stdin

def contador(matriz):
    '''La funcion hace las sumas respectivas y las agrega a una lista'''
    lista = []
    for i in range(1,5):
        for j in range(1,5):
            con_1 = matriz[i][j]
            con_2 = matriz[i-1][j-1]
            con_3 = matriz[i-1][j]
            con_4 = matriz[i-1][j+1]
            con_5 = matriz[i+1][j-1]
            con_6 = matriz[i+1][j]
            con_7 = matriz[i+1][j+1]
            contador = con_1 + con_2 + con_3 + con_4 + con_5 + con_6 + con_7
            lista.append(contador)
    return lista
def maxi(matriz):
    '''La funcion pide la nueva lista a la funcion contador, aqui la evalua y retorna el
    valor maximo'''
    new = contador(matriz)
    new.sort()
    return new[-1]
def RvD():
    '''La funcion principal, recibe los valores de cada linea y los agrega a una matriz'''

    matriz = []
    a = list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(a)
    b =list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(b)
    c =list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(c)
    d =list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(d)
    e =list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(e)
    f =list(map(int, stdin.readline().strip().split(" ")))
    matriz.append(f)
    print(maxi(matriz))
RvD()

