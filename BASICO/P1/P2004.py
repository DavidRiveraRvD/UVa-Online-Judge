#20902018

from sys import stdin

'''Para la solucion del Sudoku tuve en cuenta que la suma de los elementos de cada una de las filas y la suma
de cada uno de los elementos de cada una de las columnas tenia que dar igual a 45 de lo contrario el sudoku estaba mal'''



def RvD():
    n = int(stdin.readline())

    '''Este ciclo permite evaluar el numero de casos que ingresan'''
    
    while n != 0:

        '''Creador de sudoku: Lo hace pidiendo la linea de la fila la cual la agrega como una
        lista a una nueva lista llamada "Sudoku"'''
        
        sudoku = []
        for i in range (9):
            fila = list((stdin.readline().strip().split(" ")))
            sudoku.append(fila)
        

        '''Validador de fila, esta parte del codigo suma los elementos de la fila y si la suma es igual
        a 45 agrega un elemento "True" para este caso a una nueva lista validador_fila de lo contrario no agregara nada'''
        
        validador_fila = []
        for i in sudoku:
            conta = 0
            for j in i:
                if int(j)>0 and int(j)< 10:
                    conta += int(j)
            if conta == 45:
                validador_fila.append(True)

        '''Validador de columna, esta parte del codigo suma los elementos de la columna y si la suma es igual
        a 45 agrega el valor de "True"  a una nueva lista llamada validador_col de lo contrario no agregara nada'''
                
        validador_col = []
        pos = 0
        for i in range (9):
            cont = 0
            for i in sudoku:
                if int(i[0]) < 10 and int(i[0])>0:
                    cont += int(i[0])
            if cont == 45:
                validador_col.append(True)
            pos += 1

    
        '''Por ultimo evalua si las listas "validador_col y validador_fila" son de la longitud de 9 para imprimir lo deseado'''
        
        if len(validador_col) == 9 and len(validador_fila) == 9:
            print("Perfecto!")
        else:
            print("Incorrecto!")
        
        n -=1     
                
            
RvD()
'''DiseÃ±ado por RvD: Rivera Vargas David'''
