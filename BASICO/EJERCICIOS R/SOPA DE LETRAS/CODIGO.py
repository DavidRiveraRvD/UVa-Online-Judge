from sys import stdin

def sopa_impresion(sopa):
    '''La funcion y el ciclo permiten imprimir la sopa de letras'''
    print(str(20*"*°")+("JUEGO SOPA DE LETRAS")+str(20*"°*"))
    print("Instrucciones de juego: Para indicar la posicion que le piden tiene que tener en cuenta que las posiciones comiezan de (0,0) y van en orden ascende de izquierda a derecha, y de arriva a abajo como se muestran por pantalla en la sopa.")
    print("")
    print(26*" ", "0 1 2 3 4 5 6 7 8 9")
    print(27*" ", end = "")
    print(12*"_")
    cont = 0
    for i in sopa:    
            if  sopa.index(i) == (len(sopa)-1):
                print(21*" ", cont, "  |", end = "")
                print(*i, "|")
                print(27*" ", end = "")
                print(12*"_")
                print("")
            else:
                print(21*" ", cont, "  |", end = "")
                print(*i, "|")
                cont += 1
                
def main():
    sopa = [["a", "f", "u", "n", "c", "i", "o", "n", "s"], ["f", "e", "r", "n", "o", "d", "a", "v", "w"], ["d", "u", "v", "a", "n", "a", "n", "l", "h"], ["c", "h", "a", "n", "d", "a", "j", "o", "i"], ["r", "o", "p", "c", "i", "c", "l", "o", "l"], ["n", "ñ", "i", "o", "c", "h", "k", "p", "e"], ["c", "o", "m", "l", "i", "s", "t", "s", "a"], ["p", "e", "b", "o", "o", "p", "t", "i", "e"], ["r", "u", "s", "i", "n", "a", "s", "l", "o"]]
    palabras = ["funcion", "condicion", "uva", "while", "loops", "ciclo", "pimb", "lists"]
    encontradas = []
    sopa_impresion(sopa)
    intentos = 1
    while len(palabras) != 0:
        print("Escriba la posicion de la primera letra de la palabra con el orden Fila-Columna")
        fil, col = stdin.readline().strip().split(" ")
        print("Escriba la posicion de la ultima letra de la palabra con el orden Fila-Columna")
        fil_1, col_1 = stdin.readline().strip().split(" ")
        fil = int(fil)
        col = int(col)
        fil_1 = int(fil_1)
        col_1 = int(col_1)
        if fil > 8 or fil_1 > 8 or col > 8 or col_1 > 8:
            print("Fuera de Rango")
            print("Llevas "+str(intentos)+" intento"+"(s)")
            print(50*"*", "\n")
            intentos += 1
        else:
            if fil_1 == fil:
                palabra = ""
                for i in range((col), (col_1+1)):
                    palabra += sopa[fil][i]
                for j in palabras:
                    if j == palabra:
                        print("\nPalabra encontrada")
                        encontradas.append(palabra)
                        print("\nSus palabras encontradas son: ", end = "")
                        print(*encontradas)
                        print("Llevas "+str(intentos)+" intento"+"(s)")
                        palabras.remove(j)
                        print("\n", 90*"*", "\n")
                        intentos += 1
                        break
                    
                    elif palabras.index(j) == (len(palabras)-1):
                        print("\nPalabra no encontrada sigue intentando")
                        print("\nSus palabras encontradas son: ", end = "")
                        print(*encontradas)
                        print("Llevas "+str(intentos)+" intentos")  
                        print("\n", 90*"*", "\n")
                        intentos += 1
                        
            else:
                if col == col_1:
                    palabra = ""
                    for i in range((fil), (fil_1+1)):
                        palabra += sopa[i][col]
                    for j in palabras:
                        if j == palabra:
                            print("\nPalabra encontrada")
                            encontradas.append(palabra)
                            print("\nSus palabras encontradas son: ", end = "")
                            print(*encontradas)
                            print("Llevas "+str(intentos)+" intento"+"(s)")
                            palabras.remove(j)
                            print("\n", 90*"*", "\n")
                            intentos += 1
                            break
                        elif palabras.index(j) == len(palabras):
                            print("\nPalabra no encontrada sigue intentando")
                            print("\nSus palabras encontradas son: ", end = "")
                            print(*encontradas)
                            print("Llevas "+str(intentos)+" intentos")  
                            print("\n", 90*"*", "\n")
                            intentos += 1
                else:
                    print("\nPalabra no encontrada sigue intentando")
                    print("\nSus palabras encontradas son: ", end = "")
                    print(*encontradas)
                    print("Llevas "+str(intentos)+" intentos")
                    print("\n", 90*"*", "\n")
                    intentos += 1
                        
    print("Terminaste\nPalabras encontradas: ", end= "")
    print(*encontradas)
    print("\nTerminaste con "+str(intentos)+" intentos")    
            
main()
