from sys import stdin

"""La entraada es el numero de pares de palabras a evaluar, en una sola funcion, busco
    evaluar todos los casos hasta que la funcion principal termine de interactuar con
    las entradas ya que se esta limitando al numero inicial de casos a evaluar"""
cont = int(stdin.readline())
cont_1=1

def main(cont,cont_1):
    if cont != 0:
        x = stdin.readline()
        y = stdin.readline()
        z=x.replace(" ","")
        if x == y:
            print("Case",str(cont_1)+": Yes" )
        
        elif z == y:
            print("Case",str(cont_1)+": Output Format Error" )
            
        else:
            print("Case",str(cont_1)+": Wrong Answer" )
        return main(cont-1,cont_1+1)

main(cont,cont_1)

