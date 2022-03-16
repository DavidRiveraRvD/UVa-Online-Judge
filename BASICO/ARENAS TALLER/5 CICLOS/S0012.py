from sys import stdin

def evaluador(var,cont):
    '''Funcion que hace la multiplicacion y retorna el valor de la multiplicacion'''
    x = int(var[0])*cont
    return x
    
    


def main():
    '''Funcion principal en la que ingresan los numeros'''
    var = stdin.readline().strip().split(" ")
    cont = int (var[1])
    cont_1 = 0
    while int(var[2])+1 != cont:
        y = evaluador(var,cont)
        print("{} x {} = {}".format(var[0], cont, y))
        cont += 1
        cont_1 += 1
main()
