from sys import stdin

def valores(lista, z,conta):
    '''La funcion secundaria mediante recursiones cambia los valores para
    generar la "L" de la matriz que se desea'''
    while conta != 0:
        lista.remove(str(z))
        lista.append(str(z-1))
        conta -= 1
        return valores(lista, z, conta)
    return lista

def main():
    '''La funcion principal, recibe como parametros el numero
    de la secuencia de la matriz, crea la lista principal y la imprime'''
    x = int(stdin.readline())
    lista = []
    for i in range(1, x+1):
            lista.append(str(i))
    print((" ").join(lista))
    cont = x-1
    z = x
    conta = 1
    '''El ciclo imprime las matrices retornadas por la segunda funcion
    hasta que cumple su ciclo'''
    while cont != 0:
        l = valores(lista, z,conta)
        print((" ").join(l))
        z -=1
        cont -=1
        conta +=1
main()
        
