from sys import stdin

def evaluador(equi, equi_2, cont_1, cont_2):

    '''La funcion evalua las habilidades de los equipos he imprime
    el nombre del equimo mas habil, de lo contrario si son igual de buenos,
    monstrara por pantalla un "Empate"'''
    
    if cont_1 > cont_2:
        print(equi)
    elif cont_1 == cont_2:
        print("Empate")
    else:
        print(equi_2)
def main():

    '''La funcion principal recibe los nombres de los jugadores y de los equipos,
    suma las habilidades de los jugadores y resta la defensa del ataque y asi los
    envia a unos contadores que luego seran comparados en la segunda funcion'''
    
    equi = stdin.readline().strip()
    arque = stdin.readline().strip()
    cont_1 = 0
    conta_1 = 0
    for i in range(6):
        jud = list(stdin.readline().strip().split(" "))
        jud = jud[1::]
        cont_1 += int(jud[0])
        conta_1 += int(jud[1])

    equi_2 = stdin.readline().strip()
    arque_2 = stdin.readline().strip()

    cont_2 = 0
    conta_2 = 0
    for i in range(6):
        jud_2 = list(stdin.readline().strip().split(" "))
        jud_2 = jud_2[1::]
        cont_2 += int(jud_2[0])
        conta_2 += int(jud_2[1])
    cont_1 = cont_1-conta_1
    cont_2 = cont_2-conta_2
  
    evaluador(equi, equi_2, cont_1, cont_2)
main()
