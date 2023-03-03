def lista_con_máximos(lista):
    máximos = [max(i) for i in lista]
    return máximos

def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(lista_con_máximos([[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]))

print(list(filter(es_primo,[3, 4, 8, 5, 5, 22, 13])))
