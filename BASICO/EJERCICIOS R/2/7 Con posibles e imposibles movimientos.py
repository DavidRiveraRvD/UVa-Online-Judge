from sys import stdin

def op_1(var):
    if var[0] == "0" and (var[1] == "1" or var[1] == "0") and (var[6]=="1" or var[6] == "0") and var[7]=="0":
        return ("Frente Izquierda 45°")
    else:
        return("Imposible moverse: Frente Izquierda 45°")

def op_2(var):
    if var[0] == "0" and var[1] == "0":
        return("Frente")
    else:
        return("Imposible moverse: Frente")
        
def op_3(var):
    if (var[0] == "1" or var[0] == "0") and var[1] == "0" and var[2] == "0" and (var[3] == "1" or var[3]=="0"):
        return("Frente Derecha 45°")
    else:
        return("Imposible moverse: Frente Derecha 45°")
    
def op_4(var):
    if var[2] == "0" and var[3] == "0":
        return("Derecha 90°")
    else:
        return("Imposible moverse: Derecha 90°")

def op_5(var):
    if (var[2] == "1" or var[2] == "0") and var[3] == "0" and var[4] == "0" and (var[5] == "1" or var[5] == "0"):
        return ("Atras Derecha 45°")
    else:
        return("Imposible moverse: Atras Derecha 45°")
    
def op_6(var):
    if var[4] == "0" and var[5] == "0":
        return("Atras")
    else:
        return("Imposible moverse: Atras")
    
def op_7(var):
    if (var[4] == "1" or var[4] == "0") and var[5] == "0" and var[6] == "0" and (var[7] == "1" or var[7] == "0"):
        return("Atrás Izquierda 45°")
    else:
        return("Imposible moverse: Atrás Izquierda 45°")
    
def op_8(var):
    if var[6] == "0" and var[7] == "0":
        return("Izquierda 90°")
    else:
        return("Imposible moverse: Izquierda 90°")
def main():
    var = (stdin.readline().strip().split())
    op_1(var)
    op_2(var)
    op_3(var)
    op_4(var)
    op_5(var)
    op_6(var)
    op_7(var)
    op_8(var)
    print(op_1(var))
    print(op_2(var))
    print(op_3(var))
    print(op_4(var))
    print(op_5(var))
    print(op_6(var))
    print(op_7(var))
    print(op_8(var))
main()
