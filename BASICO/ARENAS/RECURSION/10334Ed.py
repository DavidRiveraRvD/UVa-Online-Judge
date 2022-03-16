from sys import stdin

def operador(var):
    if var == 1:
        return 2
    if var == 0 or var == 1:
        return 1
    else:
        
        return(operador(var-1)+ operador(var-2))
def main():
    var = int(stdin.readline())
    print(operador(var))
main()
