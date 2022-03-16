from sys import stdin
cont_2 = int(stdin.readline())
def evaluador(x, cont, cont_1):
    if x[-1] == "X" and len(x) == 1:
        return cont
    elif x[-1] == "O" and len(x) == 1:
        cont = 1 + cont_1 + cont
        return cont
    else:
        if x[0] == "X":
            x = x[1:]
            cont_1 = 0
            return evaluador(x, cont, cont_1)
        else:
            cont_1 += 1
            cont = cont_1 + cont
            x = x[1:]
            return evaluador(x, cont, cont_1)
 
def main(cont_2):

    if cont_2 != 0:
        x = stdin.readline().strip()
        
        cont = 0
        cont_1 = 0
        print(evaluador(x, cont, cont_1))
        cont_2 -= 1
        return main(cont_2)
    else: return

main(cont_2)
