def imprime_valores(x):
    cont = 1
    while cont <= x:
        cont2 = 2
        cont_str2 = str(cont)
        while cont2 <= cont:
            cont_str = str(cont-1)
            cont_str2 += (cont_str)
            cont2 += 1
        print(cont_str2)
        cont += 1


def teste(x):
    texto = ''
    for i in range(1, x + 1):
        texto += f' {i}'
        print(texto.strip()[::-1])


teste(6)
