from sys import stdin

def evaluador(lista, x, cont):
    '''Funcion que recursivamente busca la posicion de la fruta que se necesita
    en la lista, la funcion retorna la posicion en caso de no estar, retorna "Error!"'''
    
    if lista[cont] == x:
        return cont
    elif len(lista) == cont+1:
        return "Error!"
    else:
        cont += 1
        return evaluador(lista, x, cont)

def main():
    '''Funcion principal, evalua he imprime el valor retornado por la funcion secundaria'''
    lista = ["pera", "manzana", "mango"]
    x = stdin.readline().strip()
    cont = 0
    z = evaluador(lista, x, cont)
    print(z)
main()
