from sys import stdin




def main():
    '''La funcion inicializa con los valores "Binarios Y Hexadecimales" con sus respectivos valores'''
    
    abecedario = ["A" ,"B", "C", "D" ,"E" ,"F" ,"G" ,"H" ,"I","J", "K", "L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T", "U", "V", "W", "X" ,"Y" ,"Z" ,"a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h", "i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y", "z" ,"0" ,"1", "2", "3", "4", "5" ,"6", "7", "8" ,"9","+" ,"/"]
    binarios = ["000000","000001","000010","000011", "000100", "000101", "000110", "000111", "001000", "001001", "001010", "001011" ,"001100" ,"001101","001110", "001111" ,"010000", "010001", "010010" ,"010011" ,"010100" ,"010101" ,"010110" ,"010111" ,"011000", "011001", "011010" ,"011011" ,"011100" ,"011101", "011110" ,"011111" ,"100000" ,"100001", "100010", "100011" ,"100100", "100101", "100110", "100111" ,"101000" ,"101001", "101010" ,"101011", "101100" ,"101101", "101110" ,"101111", "110000", "110001" ,"110010", "110011", "110100" ,"110101" ,"110110" ,"110111", "111000" ,"111001", "111010" ,"111011" ,"111100", "111101" ,"111110" ,"111111"]
    binarios_2 = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    hexadecimal = ["0","1","2","3","4","5","6","7","8","9","A" ,"B", "C", "D" ,"E" ,"F"]
    x = stdin.readline().strip()
    
    while x != "*":
        '''El ciclo termina cuando el "*" aparece en la entrada de lineas adicionalmente tiene unos contadores que aran la funcion de crear los str's para asi imprimir
    los valores deceados'''
        
        new = ""
        new_2 = ""
        new_3 = ""
        contadorigual = 0
        while len(x) %4 != 0:
            '''Este ciclo cumple la finalidad de agrupar la lista de decimales'''
            f = len(x)%4
            x = x+(f*"=")
        for i in x:
            if i == "=":
                new += i
                contadorigual += 2
            else:
                a = abecedario.index(i)
                b = binarios[a]
                new +=b
        cont = 0
        
        for i in range(len(new)-contadorigual):
            '''Este ciclo recorre la cadena de decimales para finalmente convertirla en hexadecimales'''
            cont += 1
            if cont % 4 == 0:
                new_2 += new[i]
                c = binarios_2.index(new_2)
                d = hexadecimal[c]
                new_3 += d
                new_2 = ""
                cont = 0
            else:
                new_2 += new[i]
            
        print(new_3)      
        x=stdin.readline().strip()
        

main()
            
