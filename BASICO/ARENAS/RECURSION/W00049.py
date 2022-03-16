from sys import stdin

def operador(var):
    if var == 1:
        return 2
    elif var == 0:
        return 1
    else:
        return (operador(var-1)+var+var-2)


def main():
    var = int(stdin.readline())
    print(operador(var), "regiones")
main()
