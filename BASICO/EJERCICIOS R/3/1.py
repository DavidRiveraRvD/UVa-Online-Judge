from sys import stdin

def evaluador_sum(num, cont):
    '''La funcion recibe como parametros la lista de valores y un contador, la lista es invocada
    solamente cuando el operador a realizar es "+" ya que se condicionoen la funcion principal'''
    if len(num) == 1:
        return num[-1]+cont
    else:
        cont += num[-1]
        num = num[0: -1]
        return evaluador_sum(num, cont)

def evaluador_res(num, cont):
    '''La funcion recibe como parametros la lista de valores y un contador, la lista es invocada
    solamente cuando el operador a realizar es "-" ya que se co0ndicionoen la funcion principal'''
    if len(num) == 1:
        res = cont - num[0] 
        return res
    if cont == 0:
         cont = num[0]
         num = num[1::]
         return evaluador_res(num, cont)
    else:
        cont -= num[0]
        num = num[1::]
        return evaluador_res(num, cont)

def evaluador_mul(num, cont):
    '''La funcion recibe como parametros la lista de valores y un contador, la lista es invocada
    solamente cuando el operador a realizar es "*" ya que se condicionoen la funcion principal'''
    if len(num) == 1:
        return num[-1]*cont
    else:
        cont *= num[-1]
        num = num[0: -1]
        return evaluador_mul(num, cont)

def evaluador_div(num, cont):
    '''La funcion recibe como parametros la lista de valores y un contador, la lista es invocada
    solamente cuando el operador a realizar es "/" ya que se condicionoen la funcion principal'''
    if num[0] != 0:
        if len(num) == 1:
            return num[-1]/cont
        elif cont == 0:
            cont = num[0]
            num = num[1::]
            return evaluador_div(num, cont)
        else:
            cont /= num[0]
            num = num[1::]
            return evaluador_div(num, cont)
    else:
        return "Imposible dividir por 0"
    

def main():
    num = stdin.readline().strip().split(" ")
    num = list( map(int, num))
    op = stdin.readline().strip()
    if op == "+":
        cont = 0
        print(evaluador_sum(num, cont))
    elif op == "-":
        cont = 0
        print(evaluador_res(num, cont))
    elif op == "*":
        cont = 1
        print(evaluador_mul(num, cont))
    else:
        cont = 0
        print(evaluador_div(num, cont))
main()
