from sys import stdin
def listados(x):
    '''Esta funcion crea la segunda parte de la lista principal, que
    es el orden descendente de la lista que va a mostrar en la primera impresion
    y la retornara a la funcion"listadef"'''
    lista_2 = []
    cont = x//2
    for j in range(0, x//2):
        lista_2.append(cont)
        cont -= 1
    return lista_2

def listauno(x):
    '''La funcion crea la lista  en orden ascendente que la retornara a la
    funcion "listadef"'''
    lista_1 = []
    y = (x%2)+(x//2)
    for i in range(1, y+1):
        lista_1.append(i)
    return lista_1

def listadef(x):
    '''Despues de que esta funcion invoca a las don anteriores, los elementos
    de la lista descende se los agrega a la lista ascendente y la retorna a la funcion
    principal'''
    lista_d = listauno(x)
    lista_s = listados(x)
    for i in lista_s:
        lista_d.append(i)
    return lista_d
def RvD():
    x = int(stdin.readline())
    
    '''Llamados de funciones'''
    y = listadef(x)
    z = max(y)

    '''Despues de hacer los llamados de las funciones
    los siguientes condicionales imprimiran el resto de lineas que se desean en el
    codigo'''
    if x %2 == 0:
        for i in range(z+1):
            print(*y)
        v = (x//2)
        while v != 1:
            b = max(y)
            for j in y:
                if j == b:
                    c = y.index(j)
                    y.remove(j)
                    y.insert(c, b-1)
            print (*y)
            v-= 1
       
    else:
        for i in range(z):
            print(*y)
        v = (x//2+1)
        while v != 1:
            
            b = max(y)
            for j in y:
                if j == b:
                    c = y.index(j)
                    y.remove(j)
                    y.insert(c, b-1)
            print(*y)
            v-= 1
        
RvD()
'''-------------------------By: RvD // Rivera Vargas David-------------------------'''
        
    
