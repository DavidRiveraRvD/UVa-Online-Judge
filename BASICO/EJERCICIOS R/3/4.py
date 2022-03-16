from sys import stdin

def evaluador(var, cont, contt):
    '''La funcion retorna el valor final, calculado por recursiones, el valor
    es el numero entero de la evaluacion de los numeros binarios'''
    
    if (cont) == (len(var)*(-1)):
        contt += int(var[cont])*(2**-(cont+1))
        return contt
    else:
        contt += (int(var[cont]))*(2**-(cont+1))
        cont += -1
        return evaluador(var, cont, contt)
    
def main():
    '''La funcion recibe los numeros binarios, he imprime el numero representado
    por los enteros'''
    var = stdin.readline().strip().split(" ")
    cont = -1
    contt = 0
    print(evaluador(var, cont, contt))
main()

    
