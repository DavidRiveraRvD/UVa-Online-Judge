#20902018
from sys import stdin


def RvD():
    n = int(stdin.readline())

    '''El ciclo permite terminar el numero de casos cuando es 0'''
    
    while n != 0:
        '''La entrada de valores la convierte en entero'''
        
        valores = [int(x)for x in stdin.readline().strip().split(" ")]

        '''A los valores ingresados los modifique haciendo que el ultimo elemento de
        la lista inicial lo copie y lo ponga en el inicio y asi con el ultimo'''
        
        valores.append(valores[0])
        valores.insert(0, valores[-2])
        new = 0
        picos = 0
        valor = 0
        '''El ciclo suma el numero de picos en la nota'''
        
        for i in range(1, len(valores)-1):
            
            i = int(i)
            a = i-1
            b = i+1
            if valores[i] > valores[a] and valores[i] > valores[b]:
                picos += 1
            elif valores[i] < valores[a] and valores[i] < valores[b]:
                picos += 1
        print(picos)
        n = int(stdin.readline())
RvD()
'''Realizado por RvD. Rivera Vargas David'''
