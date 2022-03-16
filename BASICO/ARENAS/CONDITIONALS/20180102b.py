from sys import stdin
x = "Alexandra Pardo"
y = "Alirio Ruiz"
z = "Jorge Salcedo"
n = "Laura Picon"
m = "Nicolas Pabon"
r = "Sara Botero"
s = stdin.readline().strip()
def main():
    if s == x or s == y or s == z or s==n or s==m or s==r:
        if s == "Alexandra Pardo":
            print("3183247328")
        elif s == y:
            print("3157901628")
        elif s==z:
            print("3007486314")
        elif s==n:
            print("3004360113")
        elif s == m:
            print("3013324721")
        else:
            print("3115999932")
    else:
        print("Nombre No Encontrado")
main()
