from sys import stdin


def operador(num):
    '''La funcion que evalua si el numero es divisible en 7 y en 5
    al mismo tiempo, si es divisible por 7 y 5 al tiempo, retornara a la funcion principal
    el valor de "Hit" que la imprimira en la funcion principal, de lo contrario retornara "Not Hit"'''
    
    if num%7 == 0 and num%5 == 0:
        return "Hit"
    else:
        return "Not Hit"
    

def main():
    '''Funcion principal'''
    var = int(stdin.readline())
    cont = 0
    while cont != var:
        num = int(stdin.readline())
        x = operador(num)
        print(x)
        cont +=1
main()
