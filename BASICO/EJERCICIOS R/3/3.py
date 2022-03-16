from sys import stdin

def operador(x, lista):
    ''' En esta funcion va entrar el numero entero a evaluar (Volverlo a base binaria)
    la funcion va a descomponer el numero tamtas veces se pueda para encontrar el primer
    digito de la base binaria, adicionalmente cada vez que encuentra un numero, lo va
    adicionando a una nueva lista que es la que finalmente se va a monstrar por pantalla'''
    if x == 0 or x ==1:
        lista.insert(0, x)
        return lista
    else:
        lista.insert(0, x%2)
        x //= 2
        return operador(x, lista)


def main():
    ''' Aqui llegara el numero a evaluar(Voverlo binario) donde se invocara la funcion
    que hace la conversion'''
    x = int(stdin.readline())
    lista = []
    y = operador(x, lista)
    print(y)
main()
