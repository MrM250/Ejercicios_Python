def romano_a_decimal(numero):
    romanos = {'I': 1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
    entero = 0

    for i in range(len(numero)):
        if i > 0 and romanos[numero[i]] > romanos[numero[i-1]]:
            entero += romanos[numero[i]] - 2 * romanos[numero[i-1]]
        else:
            entero += romanos[numero[i]]

    return entero

numero = input("Introduce un Numero Romano: ")
print(romano_a_decimal(numero))