from sys import stdin


def evaluador(i, var):
    '''La funcion recibee como parametros, un contador "i" que trae consigo
    el numero de caracteres a imprimir o mostrar por pantalla, los muestra por
    pantalla recursivamente'''
    if i == 1:
        print(var[-1])
    else:
        print(var[-1], end = ' ')
        i -=1
        return evaluador(i, var)
def main():
    '''Funcion principal, evalua he imprime los valores deseados de la piramide''' 
    var = stdin.readline().strip().split('-')
    cont = 1
    while cont != int(var[0]):
        evaluador(cont, var)
        cont += 1
    while cont != 0:
        evaluador(cont, var)
        cont -= 1
    
main()
