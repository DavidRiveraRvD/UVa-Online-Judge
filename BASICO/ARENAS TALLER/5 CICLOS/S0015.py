from sys import stdin

def main():
    '''Esta funcion permite crear una lista, modificarla, he imprimirla finalmente'''
    x = int(stdin.readline())
    lista = []
    for i in range(1,x+1):
        lista.append(str(i))
    print((' ').join(lista))
    for i in range(x-1):
        lista=lista[:-1]
        lista.insert(0,str(int(lista[0])+1))
        print((' ').join(lista))
        
main()
