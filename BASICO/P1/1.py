from sys import stdin

def centenas(var_2, n):
    if (int(var_2)) == 0:
        return False
    else:
        q = int(int(n)//int(var_2))
        return q
    
def decenas(var_3, n):
    if (int(var_3)) == 0:
        return False
        
    else:
        w =  int(int(n)/int(var_3))
        return w
    
def dop(var_1, var_2, n, var_4, var_3):

    if (int(var_4)) == 0:
        return False
    else:
        r = (int(var_1))*10
        t = int(r)+(int(var_2))
        w =  int(t)%(int(var_4))
        return w
def digitos(var_1, var_2, var_3, var_4):
    d = (int(var_1))+(int(var_2))+(int(var_3))+(int(var_4))
    return d
    
def main():
    n = stdin.readline()
    var_1 = (n[-4])
    var_2 = (n[-3])
    var_3 = (n[-2])
    var_4 = (n[-1])
    
    centenas(var_2, n)
    decenas(var_3, n)
    dop(var_1, var_2, n, var_4, var_3)
    digitos(var_1, var_2, var_3, n,var_4, var_3)
    y = centenas(var_2, n)
    u = decenas(var_2, n)
    i = dop(var_1, var_2, n, var_4, var_3)

    if y == False:
        print("Error de centenas")
    elif u == False:
        print("Erorr de decenas")
    elif i == False:
        print("Erorr de unidades")
    else:
        y = centenas(var_2, n)
        u = decenas(var_2, n)
        i = dop(var_1, var_2, n, var_4)
        l = y + u + i
        suma = digitos(var_1, var_2, var_4, var_3)
        resul = round((l/suma),2)
        print(resul)
    
   

main()
    
