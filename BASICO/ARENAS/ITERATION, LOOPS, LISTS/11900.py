from sys import stdin



def main():
    '''La funcion principal recibe el numero de casos, con un While evalua
    el numero de casos'''
    
    x = int(stdin.readline())
    cont = 1
    while x != 0:
        n, p, q = stdin.readline().strip().split(" ")
        mg = list(map(int, stdin.readline().strip().split(" ")))
        numero = 0
        peso = 0
        i = 0
        '''Con otro while interactua en la lista de peso de huevos
        hasta que se rompa el ciclo, y suma el numero de huevos posibles hasta
        el momento'''
        while numero < int(p) and i < len(mg):
            peso += mg[i]
            i +=1
            if peso <= int(q):
                numero +=1
        '''Finalmente imprime el resultado'''
        
        print("Case {}: {}".format(cont, numero))
        cont +=1
        x -=1
main()
