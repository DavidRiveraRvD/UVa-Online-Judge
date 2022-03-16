global cont
cont = 0
def quickSort(x):
    global cont
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                cont += 1
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quickSort(x[:i])
        second_part = quickSort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
        
alist = [1,2,3]
quickSort(alist)
print(cont)
