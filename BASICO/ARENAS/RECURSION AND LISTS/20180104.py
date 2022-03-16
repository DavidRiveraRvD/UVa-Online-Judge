from sys import stdin

def evaluador(var, x, i):
    """Aqui el numero entra para ser evaluado, tantas veces sea necesario para
    ser recurrente y para que la funcion principal lo evalue"""
    
    if len(var)==1:
        return int(var)
    else:
        if len(var) == i:
            return(evaluador(str(x), 1, 0))
        else:
            x *= int(var[i])
            
            return(evaluador(var, x, i+1))
            
def main():
    var = stdin.readline().strip()
    x = 1
    i = 0
    """El numero que retorna de la funcion de evaluador, es evaluado
    e imprime la evaluacion del numero"""
    if evaluador(var, x, i) == 0:
        print("Numero Neto")
    else:
        print("No es un Numero Neto")
main()
