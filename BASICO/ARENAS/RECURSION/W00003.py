from sys import stdin

def operador(var):
    if var == 1:
        print(var)
        return 1
    else:
        print(var)
        return(operador(var//2))
def main():
    var = int(stdin.readline())
    operador(var)
main()
