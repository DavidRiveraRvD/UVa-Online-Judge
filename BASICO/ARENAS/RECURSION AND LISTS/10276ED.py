from sys import stdin



def operador(var):
    """El numero a evaluar entra para cumplir con su recurrencia acudiendo
    siempre a un caso base del cual va partir la secuencia""" 
    if var == 1:
        return 1
    else:
        return operador(var-1)+var+var%2

def main():
    """La funcion principal, recibe e invoca a la funcion evaluador para
    imprimir el resultado final"""
    var = int(stdin.readline())
    print(operador(var))
main()
