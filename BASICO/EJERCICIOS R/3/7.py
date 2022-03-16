from sys import stdin

def multiplicacion(num, num_1, cont):
    '''La funcion mediante sumas y recursiones calcula la mulriplicacion deseada'''
    
    if num == 1:
        cont += num_1
        return cont
    else:
        cont += num_1
        num -= 1
        return multiplicacion(num, num_1, cont)
    
def division(num, num_1, cont):
    '''La funcion retorna el valor deseado de la division por medio de
    restas recursivas'''
    if num == num_1:
        return cont+1
    elif num < num_1:
        print (cont*cont, num)
        return False
    else:
        num -= num_1
        cont += 1
        return division(num, num_1, cont)
    
def main():
    '''La funcion principal recibe las entradas y las envia a una funcion dependiendo
    del signo de la operacion,para posteriormente monstrarlas por pantalla'''
    
    op, num, num_1 = stdin.readline().strip().split(" ")
    num = int(num)
    num_1 = int(num_1)
    if op == "x":
        cont = 0
        y = multiplicacion(num, num_1, cont)
        print(y)
    elif op == "/":
        cont = 0
        y = division(num, num_1, cont)
        if y == False:
            pass
        else:
            print(y)
    else:
        print("Error de operador, solo multiplicacion 'x' o division '/'")
main()
