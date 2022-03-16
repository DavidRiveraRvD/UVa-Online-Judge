from sys import stdin

def operador(var):
    if var == 1:
        return 4
    else:
        return (operador(var-1)*-2)
def main():
    x = int(stdin.readline())
    print(operador(x))
main()
