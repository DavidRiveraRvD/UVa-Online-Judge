from sys import stdin

def contactos(campos):
    x = input("Ingrese los contactos que quiere guardar: ")
    x = int(x)
    agenda = { }
    for i in range(x):
        agenda.setdefault(i+1, { })
        for j in campos.keys():
            if campos[j] == 1:
                r = input(str("Ingrese ") +str (j) +str (": "))
                agenda[i+1].setdefault(j, r)
    return agenda

def modificar(agenda, campos):
    contacto = input("Ingrese nombre del contacto: ")
    for cont, h in enumerate(agenda.items()):
        if h[1].get("Nombre", "Error") == contacto:
            campo = input("Ingrese campo a modificar: ").lower()
            if campos.get(campo, -1):
                print("Campo no existe")
            elif campos.get(campo, -1) == 0:
                print("Campo no habilitado")
            else:
                valor = input("Ingrese nuevo valor para "+str(campo))
                agenda[cont+1][campo] = valor
    return agenda

def visualizar(agenda):
    for i in agenda.values():
        print("+"*5, "USUARIO", i+1, "+"*5)
        for j in i.items():
            print()

    
def RvD():
    campos = {'Nombre': 1, 'Apellido': 1, 'Telefono': 1, 'Correo':1}
    habilitado = False
    while True:
        print("-"*5, "AGENDA", "-"*5)
        print("1. Crear agenda\n 2. modificar agenda\n 3.Visualizar agenda\n 4. Borrar agenda\n 0. Salir")
        op = int(input("..."))
        if op == 1:
            agenda = contactos(campos)
        elif op == 2:
            if habilitados:
                agenda = modificar(agenda, campos)
            
        elif op == 3:
            visualizar(agenda)
        elif op == 4:
            agenda = ()
        elif op == 0:
            break
        else:
            print("opcion incorrecta")
            
    print("Hasta luego!!!")
    
RvD()
'''BY: RvD Rivera Vargas David'''
