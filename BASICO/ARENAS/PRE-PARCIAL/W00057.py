from sys import stdin

def main():
    '''La funcion recibe las entradas de las matrices  y crea la matrix con repecto
    a esa entrada''' 
    col_a, fil_a = map(int, stdin.readline().strip().split(","))
    entrada = list(map(int, stdin.readline().strip().split(",")))
    matriz =[]
    col_b, fil_b = map(int, stdin.readline().strip().split(","))
    entrada_b = list(map(int, stdin.readline().strip().split(",")))
    matriz_b =[]
    conta = 0
    cont = 0
    if col_b == fil_a: 
        for i in range(col_a):
            s = []
            for j in range(fil_a):
                s.append(entrada[cont])
                cont += 1
            matriz.append(s)
        
        for i in range(col_b):
            s = []
            for j in range(fil_b):
                s.append(entrada_b[conta])
                conta += 1
            matriz_b.append(s)


        

        '''Multiplicacion de matrices. La multiplicacion la hace iterando en la lista de listas "Matriz"
        hasta obtener el resultado deseado'''
        
        resultados = []
        cony = 0
        for i in range(col_a):
            resultados_1 = []
            a = 0
            for j in range(fil_b):
                for k in range(col_b):
                    a += (matriz[i][k])*(matriz_b[k][j])
                resultados_1.append(a)
                a = 0
            resultados.append(resultados_1)
            
        for i in resultados:
            print(*i)
    else:
        print("Impossible")
        
main()
