from sys import stdin


def ordenamiento(lista):
    '''Esta funcion los ordena de menor a mayor'''
    
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    print(lista)

    '''Esta funcion los ordena de mayo a menor'''
    
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] < lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

    

def main():
    lista = [int(num) for num in stdin.readline().strip().split(" ")]
    print(ordenamiento(lista))
main()    
            
