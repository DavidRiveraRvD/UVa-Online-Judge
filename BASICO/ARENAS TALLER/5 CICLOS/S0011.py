from sys import stdin

def evaluador(x):
    '''La funcion retorna valores Booleanos cuando el numero es o no
    impar'''
    if x % 2 == 0:
        return True
    else:
        return False

def main():
    '''Funcion princiupal'''
    x = int(stdin.readline())
    par = 0
    impar = 0
    while x != 0:
        '''Luego de que la funcion "Evaluador" retorna el valor Booleano, lo condiciono
        y le sumo a un contador independiente para que lo evalue y al final lo muestre por pantalla'''
        y = evaluador(x)
        if y == True:
            par += 1
        else:
            impar += 1
        x = int(stdin.readline())
    print("Cantidad de pares: {}".format(par))
    print("Cantidad de impares: {}".format(impar))
    
main()
