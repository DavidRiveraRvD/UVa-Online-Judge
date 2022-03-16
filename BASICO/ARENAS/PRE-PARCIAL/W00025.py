from sys import stdin



def listas(num, lista):
    '''La funcion hace la lista y el numero y crea la matriz con las
    longitudes deeseadas para la comparacion'''
    
    matriz = []
    subgrupo = []
    for i in lista:
        subgrupo.append(i)
        if len(subgrupo)== num:
            matriz.append(subgrupo)
            subgrupo = []

    matriz_t = []

    for i in range((num)):
        a = []
        matriz_t.append(a)

    
    for i in range(len(lista)):
        if i == 0:
            matriz_t[0].append(lista[0])
        else:
            a = i%num
            matriz_t[a].append(lista[i])

    if matriz_t == matriz: print("Hadamard")
    else:print("No Hadamard")
        
        

        
             
def evaluador(num, lista):
    '''La funcion evaluador recibe la lista y el numero los cuales
    los evalua, y la envia a la funcion de listas para su
    comparacion'''
    if num == 1: print("Hadamard")
    elif num%2 == 1: print("Imposible")
    else: listas(num, lista)

def RvD():
    '''Funcion principal, recibe el numero, de la matriz y la lista
    de valores, luego llama a la funcion evaluador'''
    num = int(stdin.readline())
    lista = [x for x in stdin.readline().strip().split()]
    evaluador(num, lista)
    
RvD()
