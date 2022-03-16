from sys import stdin

"""La funcion secundaria va evaluar el numero si cumprle las condiciones de maximo comun divisor,
    donde se juega con los Mod y Div hasta encontrar el numero necesario a partir de la division entera
    del primero en el segundo y restandole uno a ese valor hasta que cumpla las condiciones"""
def evaluador(var, var_1, resul):
    if var%var_1 == 0:
        return var_1
    elif resul != 0 and var_1%resul == 0 and var%resul == 0 :
        return resul
    else:
        resul = resul - 1
        return evaluador(var, var_1, resul)

    
def main():
    var = int(stdin.readline())
    var_1 = int(stdin.readline())
    if var>var_1:
        resul = var%var_1
        print(evaluador(var, var_1, resul))
    else:
        resul = var_1%var
        print(evaluador(var_1, var, resul))     
main()
