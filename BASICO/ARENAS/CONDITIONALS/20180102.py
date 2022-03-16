from sys import stdin

a = (stdin.readline().strip())
b = (stdin.readline().strip())
c = (stdin.readline().strip())
d = (stdin.readline().strip())
e = (stdin.readline().strip())

if  (b =="1" or  b == "0") and (c =="1" or  c == "0")  and (a =="1" or  a == "0") and (d =="1" or  d == "0") and(e =="1" or  e == "0") :
    if int(a) == 1 and ((int(b) == 1 and int(c) == 0) or (int(b) == 0 and int(c)==1)) and int(d)==1 and int(e)==1:
        print ("Recorrido Valido")
    else:
        print ("Recorrido No Valido")
else:
    print("Valor Leido No Valido")
