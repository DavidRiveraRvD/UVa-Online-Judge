from sys import stdin

'''Planteo dos listas, una para letras MAYUSCULAS y otra de las MINUSCULAS,
para iterar sobre ellas'''

ABC = ['A' ,'B', 'C', 'D' ,'E' ,'F' ,'G' ,'H' ,'I','J', 'K', 'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T', 'U', 'V', 'W', 'X' ,'Y' ,'Z']
abc = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h', 'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y', 'z']

def impresion(cifrado):
    '''La funcion imprime de forma recursiva la palabra final'''
    if len(cifrado) == 1:
        print(cifrado[0])
    else:
        print(cifrado[0], end=(""))
        cifrado = cifrado[1:]
        return impresion(cifrado)
    
def main():
    '''Recibo el numero de casos y los evaluo mediante un ciclo'''
    casos = int(stdin.readline())
    con = 1
    while casos != 0:
        
        '''Asigno variables a las entradas para jugar con ellas'''
        
        pal = stdin.readline().strip()
        mov = int(stdin.readline())
        cifrado = []
        
        '''Mediante un ciclo evaluo las palabras y hago las conversiones deseadas'''
        
        for i in pal:
            if i in abc:
                pos = abc.index(i)
                pos += mov
                if pos > 25:
                    pos = pos % 26
                    letter = abc[pos]
                    cifrado.append(letter)
                else:
                    letter = abc[pos]
                    cifrado.append(letter)
            elif i in ABC:
                pos = ABC.index(i)
                pos += mov
                if pos > 25:
                    pos = pos % 26
                    letter = ABC[pos]
                    cifrado.append(letter)
                else:
                    letter = ABC[pos]
                    cifrado.append(letter)
                
            else:
                cifrado.append(i)
        print(cifrado)
        print("Case"+str(con)+" = ", end=(""))    
        impresion(cifrado)
        casos -= 1
        con += 1
        
main()
