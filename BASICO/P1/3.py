from sys import stdin

def evaluador(n_1, n_2, n_3, n_4, opa, ope):
    if opa == "+":
        if n_3 + n_4 == 0:
            print("Error!")
        elif ope == "-":
            e = (n_1 - n_2)/(n_3 + n_4)
            print("%.2f"%(e))
        elif ope == "*":
            e = (n_1 * n_2)/(n_3 + n_4)
            print("%.2f"%(e))
        elif ope == "/":
            if n_2 == 0:
                print("Error!")
            else:
                e = (n_1 / n_2)/(n_3 + n_4)
                print("%.2f"%(e))
        else:
            e = (n_1 + n_2)/(n_3 + n_4)
            print("%.2f"%(e))
    elif opa == "*":
        if n_3 * n_4 == 0:
            print("Error!")
        elif ope == "-":
            e = (n_1 - n_2)/(n_3 * n_4)
            print("%.2f"%(e))
        elif ope == "*":
            e = (n_1 * n_2)/(n_3 * n_4)
            print("%.2f"%(e))
        elif ope == "/":
            if n_2 == 0:
                print("Error!")
            else:
                e = (n_1 / n_2)/(n_3 * n_4)
                print("%.2f"%(e))
        else:
            e = (n_1 + n_2)/(n_3 * n_4)
            print("%.2f"%(e))
    elif opa == "/":
        if n_4 == 0 :
            print("Error!")
        elif ope == "-":
            e = (n_1 - n_2)/(n_3 / n_4)
            print("%.2f"%(e))
        elif ope == "*":
            e = (n_1 * n_2)/(n_3 / n_4)
            print("%.2f"%(e))
        elif ope == "/":
            if n_2 == 0:
                print("Error!")
            else:
                e = (n_1 / n_2)/(n_3 / n_4)
                print("%.2f"%(e))
        else:
            e = (n_1 + n_2)/(n_3 / n_4)
            print("%.2f"%(e))
    else: 
        if n_3 - n_4 == 0:
            print("Error!")
        elif ope == "-":
            e = (n_1 - n_2)/(n_3 - n_4)
            print("%.2f"%(e))
        elif ope == "*":
            e = (n_1 * n_2)/(n_3 - n_4)
            print("%.2f"%(e))
        elif ope == "/":
            if n_2 == 0:
                print("Error!")
            else:
                e = (n_1 / n_2)/(n_3 - n_4)
                print("%.2f"%(e))
        else:
            e = (n_1 + n_2)/(n_3 - n_4)
            print("%.2f"%(e))
def main():
    n_1, n_2, n_3, n_4 = stdin.readline().strip().split(" ")
    ope, opa = stdin.readline().strip().split(" ")
    n_1 = float(n_1)
    n_2 = float(n_2)
    n_3 = float(n_3)
    n_4 = float(n_4)
    evaluador(n_1, n_2, n_3, n_4, opa, ope)
main()
    
