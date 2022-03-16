from sys import stdin

def evaluador(var, var_1):
    print(var+var_1)
    print(var-var_1)
    print(var*var_1)


def main():
    var = int(stdin.readline().strip())
    var_1 = int(stdin.readline().strip())
    evaluador(var, var_1)
main()
