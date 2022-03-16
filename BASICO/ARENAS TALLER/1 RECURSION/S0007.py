from sys import stdin
import sys
sys.setrecursionlimit(100000)
def operador(a, b):
    
    if a == 0:
        return  b+1
    elif b == 0:
        return operador(a-1, 1)
    return operador(a-1, operador(a, b-1))


def main():
    a, b = stdin.readline().split(" ")
    a = int(a)
    b = int(b)
    print(operador(a, b))

main()
