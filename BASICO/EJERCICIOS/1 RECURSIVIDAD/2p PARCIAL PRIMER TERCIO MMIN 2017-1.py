from sys import stdin

def operador(x):
    if x == 1:
        return 10
    else:
        return((operador(x-1)*10)-9)
def main():
    x = int(stdin.readline())
    print(operador(x))
main()
