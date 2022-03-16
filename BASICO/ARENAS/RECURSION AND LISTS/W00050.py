from sys import stdin
"""La funcion secundaria evalua una lista y la va reduciendo de valores, a la vez que va
    imprimiendo los ultimos valores de la lista, hasta que la lista queda en conjunto vacio"""
    
def operador(lista):
    if len(lista) == 1:
        print(lista[-1])
    else:
        print(lista[-1], end=',')
        lista.pop()
        return operador(lista)

def main():
    lista = stdin.readline().strip().split(',')
    operador(lista)
main()
