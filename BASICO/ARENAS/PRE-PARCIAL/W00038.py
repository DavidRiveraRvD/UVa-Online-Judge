from sys import stdin

def ordenamiento_quick(total):

    '''Algoritmo de ordenamiento merge'''
    
    ret = []
    if( len(total) == 1):return total
    half  = len(total)// 2
    lower = ordenamiento_quick(total[:half]);upper = ordenamiento_quick(total[half:])
    lower_len = len(lower);upper_len = len(upper)
    i=j=0
    
    while i != lower_len or j != upper_len:
        if( i != lower_len and (j == upper_len or lower[i] < upper[j])):ret.append(lower[i]);i += 1
        else:ret.append(upper[j]);j += 1
    return ret

def inversion(impar,o):
    '''La funcion retorna la lista de impares, la cual
    la invierte de forma recursiva'''
    if len(impar)==1:
        o.insert(0, impar[0])
        return o
    else:
        o.insert(0, impar[0])
        impar = impar[1:]
        return inversion(impar,o)
def RvD():
    '''La funcion principal recibe el numero de casos
    que van a ingresar y los evalua'''
    cas = int(stdin.readline())
    
    while cas != 0:
        '''Recibo los datos en forma de lista y los ordeno,
        posteriormente los numeros pares o impares los agrego
        a una lista de dichos elementos'''
        lon = int(stdin.readline())
        lis = [int(i) for i in stdin.readline().strip().split(" ")]
        lista = ordenamiento_quick(lis)
        
        par, impar = [], []
        
        for i in lista:
            if i%2 == 0:
                par.append(i)
            else:
                impar.append(i)
                
        '''Lo condiciono para cuando solo entrarn pares o solo
        hay impares en la entrada'''
        if len(par) == 0:
            print(*impar[::-1])
        elif len(impar) == 0:
            print(*par)
        else:
            '''En caso de haber de los dos tipos invierto
            los impares en una funcion y mediante un ciclo la
            agrego a la lista par, la cual finalmete la imprimo'''
            o = []
            impar = inversion(impar, o)
            for i in impar:
                par.append(i)
            print(*par)
        
        cas -= 1

RvD()
