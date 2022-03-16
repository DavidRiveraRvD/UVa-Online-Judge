from sys import stdin

def evaluador(lista):
    '''La funcion Evaluador tiene como parametro la entrada de la palabra que nos han dado,
    los condicionales de la funcion permiten evaluar he imprimir cada letra de la palabra de
    la ultima a la primera, recursivamente'''
    if len(lista) == 1:
        print (lista[-1])
    else:
        print(lista[-1], end="")
        lista = lista [0:-1]
        return evaluador(lista)
def main():
    lista = stdin.readline().strip()
    evaluador(lista)
main()
