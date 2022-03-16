from sys import stdin
def evaluador(x):
    """La segunda funcion, evalua y compara los valores de la entrada principal "x" para retornar el valor
    al que pertenece, y asi consecutivamente cuantas veces la funcion "main" la invoque"""
    
    if x == "HELLO":
        return "ENGLISH"

    elif x == "HOLA":
        return "SPANISH"

    elif x == "HALLO":
        return"GERMAN"     
    elif x == "BONJOUR":
        return "FRENCH"
    
    elif x == "CIAO":
        return "ITALIAN"
    elif x == "ZDRAVSTVUJTE":
        return "RUSSIAN"
    else:
        return "UNKNOWN"
    
def main():
    """La funcion principal esta acompañada de un ciclo que evalua la entrada, hasta que la condicion la rompen."""
    
    x = stdin.readline().strip()
    cont = 1
    while x != "#":
        cont = str(cont)
        y = evaluador(x)
        print("Case " + cont + ":" + " " + y )
        cont = int(cont)+ 1
        x = stdin.readline().strip()
          
main()
