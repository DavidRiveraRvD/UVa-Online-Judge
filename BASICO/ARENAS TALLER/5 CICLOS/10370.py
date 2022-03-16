from sys import stdin


def main():
    '''La funcion principal recibe el numero de entradas y con un ciclo evalua
    cada entrada sumando los elementos de la misma y luego calculando el promedio,
    con el promedio evalua con otro ciclo que numeros en esa lista son mayores que el promedio
    y asi, luego de calcularlos los multiplica por 100 para obtener el resultad y los imprime
    redondeandolos a tres cifras decimales'''
    
    x = int(stdin.readline())
    while x != 0:
        var = stdin.readline().strip().split(" ")
        var = list(var)
        cont = 0
        for y in var:
            cont += int(y)
            y = int(y)+1
        cont = cont-(float(var[0]))
        cont = cont/float(var[0])
        
        new_cont = 0
        for i in range(1, len(var)):
            if int(var[i]) > cont:
                new_cont +=1
        b = (new_cont/float(var[0]))*100
        print("{0:.3f}".format(b)+"%")
        x-=1
                
main()
            
        











    
