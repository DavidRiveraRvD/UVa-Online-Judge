from sys import stdin

def main():
    '''La funcion recibe el numero de casos'''
    x = int(stdin.readline())
    g = x
    con = 0
    lista = []
    '''Por medio del ciclo permite evaluar el numero de casos sumandolos
    y enviandolos a una lista'''
    while x !=0:
        y = int(stdin.readline())
        lista.append(y)
        con += y
        x -= 1
        
    '''z es la suma de casos dividida entre el numero de casos'''
     z = con/g

     '''El ciclo toma en un contador las sumas de cada numero e la lista elevada al cuadrado'''
    cont = 0
    for i in lista:
        cont += (i-z)**2
    
    '''Finalmente el resultado es igual a la desviacion estandar'''
    resultado = ((1/g)*cont)**0.5

    '''Redondeo los valores y los imprimo por pantalla'''
    z = round(z, 2)
    resultado = round(resultado, 2)
    print("Promedio: "+str(z))
    print("D. Estandar:", resultado)
main()
