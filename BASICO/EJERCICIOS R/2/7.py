from sys import stdin

def op_1(var):
    if var[0] == "0" and (var[1] == "1" or var[1] == "0") and (var[6]=="1" or var[6] == "0") and var[7]=="0":
        print("Frente Izquierda 45°")
    else:
        pass

def op_2(var):
    if var[0] == "0" and var[1] == "0":
        print("Frente")
    else:
        pass
        
def op_3(var):
    if (var[0] == "1" or var[0] == "0") and var[1] == "0" and var[2] == "0" and (var[3] == "1" or var[3]=="0"):
        print("Frente Derecha 45°")
    else:
        pass
    
def op_4(var):
    if var[2] == "0" and var[3] == "0":
        print("Derecha 90°")
    else:
        pass

def op_5(var):
    if (var[2] == "1" or var[2] == "0") and var[3] == "0" and var[4] == "0" and (var[5] == "1" or var[5] == "0"):
        print("Atras Derecha 45°")
    else:
        pass
    
def op_6(var):
    if var[4] == "0" and var[5] == "0":
        print("Atras")
    else:
        pass
    
def op_7(var):
    if (var[4] == "1" or var[4] == "0") and var[5] == "0" and var[6] == "0" and (var[7] == "1" or var[7] == "0"):
        print("Atrás Izquierda 45°")
    else:
        pass
    
def op_8(var):
    if var[6] == "0" and var[7] == "0":
        print("Izquierda 90°")
    else:
        pass
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

main()
